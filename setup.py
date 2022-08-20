# Installation of `titans` package
from setuptools import setup, find_packages


setup(
    name="titans",
    version="0.1",
    description="Tool for the development and deployment of TensorFlow EfficientNet computer vision models.",
    author="Lucas Zhou",
    author_email="lucasfzhou@outlook.com",
    url="https://github.com/lucasfzhou/titans-ml",
    install_requires=[
        "Pillow",
        "tensorflow>=2",
        "tensorflow_hub",
    ],
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.6",
    packages=find_packages(),
    extras_require={
        "app": ["Flask", "gunicorn"],
        "dev": ["pre-commit"],
        "research": ["jupyterlab", "tensorflow_datasets", "wandb"],
    },
)