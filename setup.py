from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = "Coming soon."#fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.read().splitlines()

setup(
    name='visuallayer',
    version='0.0.15',
    url='https://github.com/visual-layer/vl-datasets',
    author='Visual Layer',
    author_email='info@visual-layer.com',
    description='Open, Clean Datasets for Computer Vision.',
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
    install_requires=requirements
)
