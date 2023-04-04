# VL-Datasets

## What?
This repo shares clean version of publicly available computer vision datasets.

## Why?
Even with the success of generative models, data quality remains an issue that's mainly overlooked.
Training models will erroneours data impacts model accuracy, incurs costs in time, storage and computational resources.

## How?
In this repo we share clean version of various computer vision datasets. We hope this effort will also help the community train better models and mitigate various model biases.

The cleaned image dataset should be free from most if not all of the following issues:

+ Duplicates.
+ Broken images.
+ Low information images (dark/bright/blurry images).

## Datasets

### Clean-ImageNet-21K
In the original ImageNet-21K dataset we find up to 15.9% of the images are problematic. Among those there are 1.2M redundant duplicate and 104K train validation leaks.

To access the clean version of ImageNet-21K, sign up [here](https://forms.gle/khZpAGUQJeqgRwwo7).

### Clean-LAION-400M
In the original LAION-400M dataset, we find 10.3M missing images (stale URLs) and 1.63M corrupted images. Common corruptions include over 772k images
having format issues and not loading, 443k images smaller
than 10x10 pixels, and over 300k images that are ’File not
found’ placeholders

To access the clean version of LAION-400M, sign up [here](https://forms.gle/khZpAGUQJeqgRwwo7).

## Disclaimer
You are bound to the usage license of the original dataset. We provide no warranty or guarantee of accuracy or completeness.