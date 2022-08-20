"""Utilities for working with imagenet_v2"""
import tensorflow as tf
import tensorflow_datasets as tfds


try:
    AUTOTUNE = tf.data.AUTOTUNE
except:
    AUTOTUNE = tf.data.experimental.AUTOTUNE


def load_imagenet_v2(target_size, batch_size):
    ds_test = tfds.load("imagenet_v2", split="test", as_supervised=True)
    print(f"Test set size: {ds_test.cardinality()}")
    return (
        ds_test.map(lambda img, label: (tf.image.resize(img, size=target_size), label))
        .map(lambda img, label: (img / 255.0, label))
        .batch(batch_size)
        .cache()
        .prefetch(AUTOTUNE)
    )