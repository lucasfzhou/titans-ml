# Research Experimentation

`titans` uses [Weights & Biases](https://wandb.ai/site) to track ML experiments.

To run an experiment, first install the research dependencies:

```bash
pip install .[research]
```

Then log in to the wandb service:

```bash
wandb login --host https://wandb.ai/site
```

## File Organization

The script `experiments/baseline.py` performs a benchmark evaluation on the
[ImageNet-v2](https://www.tensorflow.org/datasets/catalog/imagenet_v2) dataset. Try
modifying the configuration (e.g. `config.scale`) and compare performance, or create a
new experiment script for a novel strategy (it could even use a different framework
such as PyTorch!)

`utils.py` should include preprocessing and evaluation code to keep code [DRY](
https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and ensure fair comparison of
models.

`inspect.ipynb` is meant to be a scratch space where data and model predictions can be
explored in an open-ended fashion.