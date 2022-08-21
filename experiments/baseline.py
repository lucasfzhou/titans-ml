"""Baseline evaluation of ImageNet-v2"""
from pprint import pprint

import tensorflow as tf
import wandb
from titans.tfefficientnet import EfficientNet

from utils import load_imagenet_v2


try:
    AUTOTUNE = tf.data.AUTOTUNE
except:
    AUTOTUNE = tf.data.experimental.AUTOTUNE

########################################################################################
# Configuration
########################################################################################

run = wandb.init(
    project="imagenet_v2",
    entity="titansml",
    config=dict(
        model_name="efficientnet",
        scale=0,
        batch_size=32,
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    ),
)

# immutable config object!
config = wandb.config

########################################################################################
# Create model
########################################################################################

if config.model_name == "efficientnet":
    model = EfficientNet(scale=config.scale)
else:
    raise ValueError(f"Invalid model '{config.model_name}'")

model.compile(loss=config.loss, metrics=config.metrics)

########################################################################################
# Load data
########################################################################################

ds_test = load_imagenet_v2(
    batch_size=config.batch_size, target_size=model.input_shape[1:3]
)

########################################################################################
# Train
########################################################################################

# TODO if you are training the model, do it here

########################################################################################
# Save and Upload the model
########################################################################################

# TODO if you trained a model, save and upload it to wandb

# local_save_dir = os.path.join("out", run.id, "model")
# model.save(local_save_dir, overwrite=False)

# artifact = wandb.Artifact("saved_model", type="model")
# artifact.add_dir(local_save_dir)
# run.log_artifact(artifact)

########################################################################################
# Evaluate
########################################################################################

metric_names = [config.loss, *config.metrics]
metrics = dict(zip(metric_names, model.evaluate(ds_test)))
pprint(metrics)
wandb.log(metrics)