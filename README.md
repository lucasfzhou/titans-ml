# titans
Tool for the development and deployment of TensorFlow EfficientNet computer vision models.  

NOTE: This is a recreation of the course project based on initial instructions, group project, and provided example solution.

## Installation
### 1. Create and Activate Virtual Environment
Follow [this guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for any venv.  
  
Development was completed using Miniconda:  
A guide can be found at <br>
https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html <br>
or run the following: <br>
```bash
curl -OJ https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh && bash Miniconda3-py39_4.12.0-Linux-x86_64.sh
```
  
### 2. Install the `titans` package
  
To install, run the following command  
  
```bash
pip install .
```
  
Follow the [Installation for Development](CONTRIBUTING.md#Installation-for-Development) instructions for contributing to the `titans` package.  
  
## Getting Started
  
An example script can be found at [scripts/predict.py](scripts/predict.py). For usage:  
  
```bash
python scripts/predict.py -h
```
  
To run inference on the example images:  
  
```bash
python scripts/predict.py images/*
```
  
Outputted results of example images should be similar to the following:  
  
```
luce.jpg
  0: 0.149 Great Dane
  1: 0.135 American Staffordshire terrier
  2: 0.108 Border collie
  3: 0.100 bluetick
  4: 0.083 Staffordshire bullterrier

window_route.jpg
  0: 0.872 cliff
  1: 0.010 cliff dwelling
  2: 0.002 tripod
  3: 0.001 megalith
  4: 0.001 mountain bike
```
  
## Web Application
  
A lightweight Flask application is used for showcasing the `titans` package. See [app/README.md](app/README.md) for more information.  
  
## Research Experimentation
  
[Weights & Biases](https://wandb.ai/site) is used to track ML experiments of the `titans` package. See [experiments/README.md](experiments/README.md) for more information.  
  