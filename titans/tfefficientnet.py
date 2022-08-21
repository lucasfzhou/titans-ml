"""Wrapper class and related support for the EfficientNet collection of image classification models."""
from functools import lru_cache
import logging
import os
import pathlib
import urllib.request
from typing import List, Tuple

import PIL
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


logger = logging.getLogger(__name__)


# set environment variable defaults
if "TFHUB_DOWNLOAD_PROGRESS" not in os.environ:
    # tells TF Hub to log progress while downloading models
    os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "1"
if "TFHUB_CACHE_DIR" not in os.environ:
    # specifies a persistent cache location for downloaded models (the default is in
    # /tmp/... which is not persistent)
    os.environ["TFHUB_CACHE_DIR"] = os.path.expanduser("~/.cache/tfhub_modules")


@lru_cache
def get_label_map(url: str) -> Tuple[str]:
    local_path = (
        pathlib.Path(__name__)
        .absolute()
        .parent.joinpath(".cache", "label_maps", pathlib.Path(url).name)
    )

    if not local_path.exists():
        logger.info("Downloading label map to %s", local_path)
        os.makedirs(local_path.parent, exist_ok=True)
        urllib.request.urlretrieve(url, local_path)

    with open(local_path) as f:
        # skip the first (background) class
        label_map = tuple(s.strip() for s in f.readlines()[1:])

    return label_map


def preprocess(img: PIL.Image, target_size: Tuple[int, int] = None) -> tf.Tensor:
    if target_size:
        img = img.resize(target_size)
    img = tf.keras.utils.img_to_array(img, dtype=np.uint8)
    img = tf.image.convert_image_dtype(img, tf.float32)
    return img[None, ...]


def load_batch(
    img_paths: List[str], target_size: Tuple[int, int] = None
) -> Tuple[tf.Tensor, List[str]]:
    if isinstance(img_paths, str):
        img_paths = [img_paths]

    used_image_paths = []
    imgs = []

    # preprocess images individually
    for img_path in img_paths:
        try:
            img = tf.keras.utils.load_img(img_path, target_size=target_size)
        except PIL.UnidentifiedImageError:
            logger.warning("Failed to load image %s", img_path)
            continue
        imgs.append(tf.squeeze(preprocess(img)))
        used_image_paths.append(img_path)

    # stack images in a batch Tensor
    try:
        batch = tf.stack(imgs)
    except tf.errors.InvalidArgumentError as error:
        raise ValueError(
            error.message + f"\nSpecify `target_size` in load_batch() to resolve this."
        ) from error

    return batch, used_image_paths


class EfficientNet(tf.keras.Sequential):
    # the recommended height/width for each model scale (0-7)
    DEFAULT_IMAGE_SIZES = [224, 240, 260, 300, 380, 456, 528, 600]

    LABEL_MAP_URL = (
        "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"
    )

    def __init__(self, scale: int = 4, height: int = None, width: int = None):
        if not (0 <= scale <= 7):
            raise ValueError(f"Invalid scale {scale} out of range")

        height = height or self.DEFAULT_IMAGE_SIZES[scale]
        width = width or self.DEFAULT_IMAGE_SIZES[scale]

        hub_url = f"https://tfhub.dev/tensorflow/efficientnet/b{scale}/classification/1"
        super().__init__(
            layers=[hub.KerasLayer(hub_url)], name=f"EfficientNet/b{scale}"
        )

        # batch input shape
        self.build([None, height, width, 3])

        self._scale = scale

    @property
    def scale(self) -> int:
        # The EfficientNet model scale (0-7)
        return self._scale

    @property
    def label_map(self) -> Tuple[str]:
        # The string labels corresponding from integer label indices
        return get_label_map(self.LABEL_MAP_URL)

    def preprocess(self, img: PIL.Image) -> tf.Tensor:
        return preprocess(img, target_size=self.input_shape[1:3])

    def load_batch(self, img_paths: List[str]) -> Tuple[tf.Tensor, List[str]]:
        return load_batch(img_paths, target_size=self.input_shape[1:3])