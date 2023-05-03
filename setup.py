from setuptools import setup, find_packages

with open("./README.md") as f:
    long_description = f.read()

setup(
    name='vl_datasets',
    version='0.0.3',
    url='https://github.com/visual-layer/vl-datasets',
    author='Visual Layer',
    author_email='your-email@example.com',
    description='Clean datasets for computer vision.',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision"
    ]
)
