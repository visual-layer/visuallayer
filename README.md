
<!-- PROJECT LOGO -->
<br />
<div align="center">

<a href="https://www.visual-layer.com">
  <img alt="Visual Layer Logo" src="https://raw.githubusercontent.com/visual-layer/fastdup/main/gallery/visual_layer_logo.png" alt="Logo" width="400">
</a>

<h3 align="center">Open, Clean Datasets for Computer Vision</h3>

  <p align="center">
  <br />
    🔥 We use
    <a href="https://github.com/visual-layer/fastdup">fastdup</a> - a free tool to clean all datasets shared in this repo.
    <br />
    <a href="https://visual-layer.readme.io/" target="_blank" rel="noopener noreferrer"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/visual-layer/vl-datasets/issues" target="_blank" rel="noopener noreferrer">Report Issues</a>
    ·
    <a href="https://medium.com/@amiralush/large-image-datasets-today-are-a-mess-e3ea4c9e8d22" target="_blank" rel="noopener noreferrer">Read Blog</a>
    ·
    <a href="mailto:info@visual-layer.com?subject=Sign-up%20for%20access" target="_blank" rel="noopener noreferrer">Get In Touch</a>
    ·
    <a href="https://visual-layer.com/" target="_blank" rel="noopener noreferrer">About Us</a>
    <br />
    <br /> 
    <a href="https://visualdatabase.slack.com/join/shared_invite/zt-19jaydbjn-lNDEDkgvSI1QwbTXSY6dlA#/shared-invite/email" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/JOIN US ON SLACK-4A154B?style=for-the-badge&logo=slack&logoColor=white" alt="Logo">
    </a>
    <a href="https://visual-layer.readme.io/discuss" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/DISCUSSION%20FORUM-brightgreen?style=for-the-badge&logo=discourse&logoWidth=20" alt="Logo">
    </a>
    <a href="https://www.linkedin.com/company/visual-layer/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Logo">
    </a>
    <a href="https://twitter.com/visual_layer" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Logo">
    </a>
    <a href="https://www.youtube.com/@visual-layer4035" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/-YouTube-black.svg?style=for-the-badge&logo=youtube&colorB=red" alt="Logo">
    </a>
  </p>
</div>

## Description

`vl-datasets` is a collection of clean computer vision datasets, carefully analyzed and processed to avoid common image dataset issues such as:

+ Duplicates.
+ Broken images.
+ Outliers.
+ Dark/Bright/Blurry images.

## Why?

Computer vision is an exciting and rapidly advancing field, with new techniques and models emerging all the time. 
However, to develop and evaluate these models, it's essential to have reliable and standardized datasets to work with.

Even with the success of generative models, data quality remains an issue that's mainly overlooked.
Training models will erroneours data impacts model accuracy, incurs costs in time, storage and computational resources.

## Datasets
Here is a table of widely used computer vision datasets and the issues we found.

| Dataset | Issues |
| -------- | -------- |
| [Food-101](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)    | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/)    | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [Imagenette](https://github.com/fastai/imagenette)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [LAION-1B](https://laion.ai/blog/laion-5b/)  | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [Imagenet-21k](https://www.image-net.org/)  | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [Imagenet-1k](https://www.image-net.org/)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [KITTI](https://www.cvlibs.net/datasets/kitti/)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [Places365](https://github.com/CSAILVision/places365)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [CelebA-HQ](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |
| [COCO](https://cocodataset.org/#home)   | <ul><li>Duplicates - 0.24% (12,345)</li><li>Outliers - 0.85% (456)</li><li>Broken - 0.85% (456)</li><li>Blur - 0.85% (456)</li><li>Dark - 0.85% (456)</li><li>Bright - 0.85% (456)</li></ul> |

<!-- ## Setting Up

### Prerequisites 

Supported `Python` versions:


![Supported Python: Ubuntu](https://img.shields.io/badge/Python-3.9%20%7C%203.10-blue?style=for-the-badge)


Supported operating systems:

![Supported OS: Ubuntu](https://img.shields.io/badge/Supported%20OS-Ubuntu-orange.svg?style=for-the-badge) -->


## Installation

**Option 1** - Install `vl_datasets` package from PyPI.

```shell
pip install vl-datasets
```

**Option 2** - Install the bleeding edge version on GitHub
```
pip install git+https://github.com/visual-layer/vl-datasets.git@master --upgrade
```

## Usage
To start using `vl-datasets`, you can import the clean version of the dataset with:

```python
from vl_datasets import CleanFood101
```

This should import the clean version of the Food101 dataset.

Next, you can load the dataset as a PyTorch `DataLoader`.

```python
train_dataset = CleanFood101('./', split='train', exclude_csv='food_101_vl-datasets_analysis.csv', transform=train_transform)
valid_dataset = CleanFood101('./', split='test', exclude_csv='food_101_vl-datasets_analysis.csv', transform=valid_transform)
```

Now you can use the dataset in a PyTorch training loop. Refer to our sample training notebooks for details.

## Example

<table>
  <tr>
      <td rowspan="3" width="160">
      <a href="https://visual-layer.readme.io/docs/getting-started">
              <img src="./imgs/food.jpg" width="256">
      </a>
      </td>    
      <td rowspan="3">
        <b>PyTorch:</b> In this example, train a simple PyTorch model with the CleanFood101 dataset.
      </td>
      <td align="center" width="80">
          <a href="https://nbviewer.org/github/visual-layer/vl-datasets/blob/main/notebooks/train-pytorch.ipynb">
              <img src="./imgs/nbviewer_logo.svg" height="34">
          </a>
      </td>
  </tr>
  <tr>
      <td align="center">
          <a href="https://github.com/visual-layer/vl-datasets/blob/main/notebooks/train-pytorch.ipynb">
              <img src="./imgs/github_logo.png" height="32">
          </a>
      </td>
  </tr>
  <tr>
      <td align="center">
          <a href="https://colab.research.google.com/github/visual-layer/vl-datasets/blob/main/notebooks/train-pytorch.ipynb">
              <img src="./imgs/colab_logo.png" height="28">
          </a>
      </td>
  </tr>

  <!-- ------------------------------------------------------------------- -->

  <tr>
      <td rowspan="3" width="160">
      <a href="https://visual-layer.readme.io/docs/objects-and-bounding-boxes">
              <img src="./imgs/pet.jpg" width="256">
      </a>
      </td>    
      <td rowspan="3">
        <b>fastai:</b> In this tutorial learn how to train a model using fastai and timm with the CleanFood101 dataset.
      </td>
      <td align="center" width="80">
          <a href="https://nbviewer.org/github/visual-layer/vl-datasets/blob/main/notebooks/train-fastai.ipynb">
              <img src="./imgs/nbviewer_logo.svg" height="34">
          </a>
      </td>
  </tr>
  <tr>
      <td align="center">
          <a href="https://github.com/visual-layer/vl-datasets/blob/main/notebooks/train-fastai.ipynb">
              <img src="./imgs/github_logo.png" height="32">
          </a>
      </td>
  </tr>
  <tr>
      <td align="center">
          <a href="https://colab.research.google.com/github/visual-layer/vl-datasets/blob/main/notebooks/train-fastai.ipynb">
              <img src="./imgs/colab_logo.png" height="28">
          </a>
      </td>
  </tr>

  <!-- ------------------------------------------------------------------- -->
  
</table>

## License
`vl-datasets` is licensed under the Apache 2.0 License. See [LICENSE](./LICENSE).

However, you are bound to the usage license of the original dataset. It is your responsibility to determine whether you have permission to use the dataset under the dataset's license. We provide no warranty or guarantee of accuracy or completeness.
