

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.visual-layer.com" target="_blank" rel="noopener noreferrer">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./imgs/logo.png" width=400>
    <source media="(prefers-color-scheme: light)" srcset="./imgs/logo.png" width=400>
    <img alt="Fastdup logo." src="./gallery/logo.png">
    </picture>
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
    <img src="https://img.shields.io/badge/Discussion-%20Forum-brightgreen?style=for-the-badge&logo=discourse&logoColor=white" alt="Logo">
    </a>
    <a href="https://www.linkedin.com/company/visual-layer/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Logo">
    </a>
    <a href="https://www.youtube.com/@visual-layer4035" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/-YouTube-black.svg?style=for-the-badge&logo=youtube&colorB=red" alt="Logo">
    </a>
  </p>
</div>

## What?
This repo shares clean version of publicly available computer vision datasets.

## Why?
Even with the success of generative models, data quality remains an issue that's mainly overlooked.
Training models will erroneours data impacts model accuracy, incurs costs in time, storage and computational resources.

## How?
In this repo we share clean version of various computer vision datasets.

The datasets are cleaned using a free tool we released - [fastdup](https://github.com/visual-layer/fastdup).

We hope this effort will also help the community train better models and mitigate various model biases.

The cleaned image dataset should be free from most if not all of the following issues:

+ Duplicates.
+ Broken images.
+ Low information images (dark/bright/blurry images).

## Datasets

### Clean-ImageNet-21K
In the [original ImageNet-21K](https://www.image-net.org/) dataset we find up to 15.9% of the images are problematic. Among those there are 1.2M redundant duplicate and 104K train validation leaks.

We provide a subset of the original dataset by removing the aforementioned issues.
To access the clean version of ImageNet-21K, sign-up [here](https://forms.gle/khZpAGUQJeqgRwwo7).

### Clean-LAION-400M
In the [original LAION-400M dataset](https://laion.ai/blog/laion-400-open-dataset/), we find 10.3M missing images (stale URLs) and 1.63M corrupted images. Common corruptions include over 772k images
having format issues and not loading, 443k images smaller
than 10x10 pixels, and over 300k images that are ’File not
found’ placeholders

We provide a subset of the original dataset by removing the aforementioned issues.
To access the clean version of LAION-400M, sign-up [here](https://forms.gle/khZpAGUQJeqgRwwo7).

### Scripts
We provid convenience functions to help you move or delete problematic files read from a `.csv` file.

A sample content of the `.csv` file is as follows:
```
filename
buildings/0.jpg
buildings/4.jpg
```

Move problematic images to a destination folder:

```python
python scripts/move-images.py --file_paths_csv  problem_images.csv --images_dir sample_images --dest_folder_name problematic_images
```

Delete problematic images:
```python
python scripts/delete-images.py --file_paths_csv problem_images.csv --images_dir sample_images/
```


## Disclaimer
You are bound to the usage license of the original dataset. It is your responsibility to determine whether you have permission to use the dataset under the dataset's license. We provide no warranty or guarantee of accuracy or completeness.