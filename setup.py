from setuptools import setup, find_packages

setup(
    name='vl_datasets',
    version='0.0.1',
    url='https://github.com/visual-layer/vl-datasets',
    author='Visual Layer',
    author_email='your-email@example.com',
    description='Clean datasets for computer vision.',
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "pandas"
    ]
)
