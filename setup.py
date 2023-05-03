from setuptools import setup, find_packages
import sys

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='vl_datasets',
    version='0.0.15',
    url='https://github.com/visual-layer/vl-datasets',
    author='Visual Layer',
    author_email='info@visual-layer.com',
    description='Clean datasets for computer vision.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    license = "Apache-2.0",
    homepage = "https://visual-layer.com",
    documentation = "https://visual-layer.readme.io/",
    repository = "https://github.com/visual-layer/vl-datasets",
    keywords = ["machine learning", "computer vision", "data-centric"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "torch",
        "torchvision",
        "pandas"
    ]
)
