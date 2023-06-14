
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![PyPi][pypi-shield]][pypi-url]
[![PyPi][pypiversion-shield]][pypi-url]
[![PyPi][downloads-shield]][downloads-url]
[![License][license-shield]][license-url]
[![TestedOn][testedon-shield]][pypi-url]
<!-- [![Contributors][contributors-shield]][contributors-url] -->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[pypi-shield]: https://img.shields.io/badge/Python-3.7%20--%203.11-blue?style=for-the-badge
[pypi-url]: https://pypi.org/project/visuallayer/
[pypiversion-shield]: https://img.shields.io/pypi/v/visuallayer?style=for-the-badge
[downloads-shield]: https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fvisuallayer&color=lightblue
[downloads-url]: https://pypi.org/project/visuallayer/
<!-- [contributors-shield]: https://img.shields.io/github/contributors/visual-layer/fastdup?style=for-the-badge -->
<!-- [contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors -->
[license-shield]: https://img.shields.io/badge/License-Apache%202.0-purple.svg?style=for-the-badge
[license-url]: https://github.com/visual-layer/visuallayer/blob/main/LICENSE
[testedon-shield]: https://img.shields.io/badge/Tested%20on-Ubuntu--22.04%20%7C%20MacOS--10.16%20Intel%20%7C%20Windows%2010-brightgreen?style=for-the-badge


<!-- PROJECT LOGO -->
<br />
<div align="center">
<a href="https://www.visual-layer.com">
  <img alt="Visual Layer Logo" src="https://raw.githubusercontent.com/visual-layer/fastdup/main/gallery/visual_layer_logo.png" alt="Logo" width="350">
</a>
<h4 align="center">Open, Clean, Curated Datasets for Computer Vision</h4>

  <p align="center">
  <br />
    <a href="https://docs.visual-layer.com/docs/introduction-sdk" target="_blank" rel="noopener noreferrer"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/visual-layer/visuallayer/issues" target="_blank" rel="noopener noreferrer">Report Issues</a>
    ·
    <a href="https://medium.com/@visual-layer/" target="_blank" rel="noopener noreferrer">Read Blog</a>
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
    <a href="https://www.youtube.com/@visual-layer" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/-YouTube-black.svg?style=for-the-badge&logo=youtube&colorB=red" alt="Logo">
    </a>
  </p>
</div>

## Description

The `visuallayer` SDK is a pure Python and open-source package that offers access and extensibility to the cloud version of the [Visual Layer platform](https://visual-layer.link/) from your code. 

While the cloud version offers a high-level overview and visualization of your data, the SDK affords you the flexibility to integrate into your favorite machine learning frameworks and environments (e.g. Jupyter Notebook) using Python.

Using `visuallayer` you can access sanitized computer vision datasets with only 3 lines of code.

For example, to get access to the clean version of the [ImageNet-1k](https://www.robots.ox.ac.uk/~vgg/data/pets/) dataset, simply run:

![image](./imgs/usage.png)

## Dataset
When we say "sanitized", we mean that the datasets loaded by `visuallayer` are free from common issues such as:

+ Duplicates.
+ Near Duplicates.
+ Broken images.
+ Outliers.
+ Dark/Bright/Blurry images.
+ Mislabels.
+ Data Leakage.

![image](./imgs/issues.png)

We support some of the most widely used computer vision datasets.
Here are some of the datasets we currently support and the issues found using our cloud platform.

| Dataset Name    | Total Images | Total Issues (%) | Total Issues (Count) | Duplicates (%) | Duplicates (Count) | Outliers (%) | Outliers (Count) | Blur (%) | Blur (Count) | Dark (%) | Dark (Count) | Bright (%) | Bright (Count) | Mislabels (%) | Mislabels (Count) | Leakage (%) | Leakage (Count) |
|-----------------|--------------|------------------|----------------------|----------------|--------------------|--------------|------------------|----------|--------------|----------|--------------|------------|----------------|---------------|-------------------|-------------|-----------------|
| ImageNet-21K    | 13,153,500   | 14.581%          | 1,917,948            | 10.53%         | 1,385,074          | 0.085%       | 11,119           | 0.292%   | 38,463       | 0.179%   | 23,575       | 0.43%      | 56,754         | 3.06%         | 402,963           | -           | -               |
| ImageNet-1K     | 1,431,167    | 1.313%           | 17,492               | 0.57%          | 7,522              | 0.09%        | 1,199            | 0.19%    | 2,478        | 0.24%    | 3,174        | 0.06%      | 770            | 0.11%         | 1,480             | 0.065%      | 869             |
| LAION-1B        | WIP          | WIP              | WIP                  | WIP            | WIP                | WIP          | WIP              | WIP      | WIP          | WIP      | WIP          | WIP        | WIP            | WIP           | WIP               | WIP         | WIP             |
| KITTI           | 12,919       | 18.32%           | 2,748                | 15.29%         | 2,294              | 0.01%        | 2                | -        | -            | -        | -            | -          | -              | -             | -                 | 3.01%       | 452             |
| COCO            | 330,000      | 0.31%            | 508                  | 0.12%          | 201                | 0.09%        | 143              | 0.03%    | 47           | 0.05%    | 76           | 0.01%      | 21             | -             | -                 | 0.01%       | 20              |
| DeepFashion     | 800,000      | 7.89%            | 22,824               | 5.11%          | 14,773             | 0.04%        | 108              | -        | -            | -        | -            | -          | -              | -             | -                 | 2.75%       | 7,943           |
| CelebA-HQ       | 30,000       | 2.36%            | 4,786                | 1.67%          | 3,389              | 0.08%        | 157              | 0.51%    | 1,037        | 0.001%   | 2            | 0.01%      | 13             | -             | -                 | 0.09%       | 188             |
| Places365       | 1,800,000    | 2.09%            | 37644                | 1.53%          | 27,520             | 0.40%        | 7,168            | -        | -            | 0.16%    | 2,956        | -          | -              | -             | -                 | -           | -               |
| Food-101        | 101,000      | 0.62%            | 627                  | 0.23%          | 235                | 0.08%        | 77               | 0.18%    | 185          | 0.04%    | 43           | -          | -              | -             | -                 | -           | -               |
| Oxford-IIIT Pet | 7,349        | 1.48%            | 132                  | 1.01%          | 75                 | 0.1%         | 7                | -        | -            | 0.05%    | 4            | -          | -              | -             | -                 | 0.31%       | 23              |



We will continue to support more datasets. Here are a few currently in our roadmap:
+ EuroSAT
+ Flickr30k
+ INaturalist
+ SVHN
+ Cityscapes

[Let us know](https://forms.gle/8jxPkyzeKj82kPed8) if you have additional request to support a specific dataset.




<!-- ## Why?

Computer vision is an exciting and rapidly advancing field, with new techniques and models emerging now and then. 
However, to develop and evaluate these models, it's essential to have reliable and standardized datasets to work with.

Even with the recent success of generative models, data quality remains an issue that's [mainly overlooked](https://medium.com/@amiralush/large-image-datasets-today-are-a-mess-e3ea4c9e8d22).
Training models will erroneours data impacts model accuracy, incurs costs in time, storage and computational resources.

We believe that access to clean and high-quality computer vision datasets leads to accurate, non-biased, and efficient model.
By providing public access to `visuallayer` we hope it helps advance the field of computer vision. -->


## Access
The `visuallayer` SDK provides a convenient way to access the sanitized version of the datasets in Python.
Alternatively, for each dataset in this repo, we provide a `.csv` file that lists the problematic images from the dataset.

You can use the listed images in the `.csv` to improve the model by re-labeling the them or just simply remove it from the dataset.

Here is a table of datasets, link to download the `.csv` file and how to access it via `visuallayer` datasets zoo.

| Dataset Name    | Issues CSV                                       | Load with SDK                                 |
|-----------------|--------------------------------------------------|-----------------------------------------------|
| ImageNet-21K    | [![download][download-shield]][imagenet-21k-url] | `vl.datasets.zoo.load('vl-imagenet-21k')`     |
| ImageNet-1K     | [![download][download-shield]][imagenet-1k-url]  | `vl.datasets.zoo.load('vl-imagenet-1k')`      |
| LAION-1B        | [![download][download-shield]][laion-1b-url]     | -                                             |
| KITTI           | [![download][download-shield]][kitti-url]        | `vl.datasets.zoo.load('vl-kitti')`            |
| COCO            | [![download][download-shield]][coco-url]         | WIP                                           |
| DeepFashion     | [![download][download-shield]][deepfashion-url]  | WIP                                           |
| CelebA-HQ       | [![download][download-shield]][celeba-hq-url]    | WIP                                           |
| Places365       | [![download][download-shield]][places365-url]    | WIP                                           |
| Food-101        | [![download][download-shield]][food101-url]      | `vl.datasets.zoo.load('vl-food101')`          |
| Oxford-IIIT Pet | [![download][download-shield]][oxford-pets-url]  | `vl.datasets.zoo.load('vl-oxford-iiit-pets')` |


[download-shield]: https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge
[imagenet-21k-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-21K_images_issue_file_list.csv
[imagenet-1k-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-1K_images_issue_file_list.csv
[laion-1b-url]: https://google.com
[kitti-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Kitti_images_issue_file_list.csv
[coco-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Coco_images_issue_file_list.csv
[deepfashion-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/DeepFashion_images_issue_file_list.csv
[celeba-hq-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/CelebA_images_issue_file_list.csv
[places365-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Places365_images_issue_file_list.csv
[food101-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_file_list.csv
[oxford-pets-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_file_list.csv


<!-- 
<table>
   <tr>
      <th>Dataset</th>
      <th>Issues</th>
      <th>CSV</th>
      <th>Import Statement</th>
   </tr>
   <tr>
      <td><a href="./dataset_card/imagenet-21k/card.md">ImageNet-21K</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>10.53% (1,385,074)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.085% (11,119)</td>
            </tr>
            <tr>
               <td>Blur</td>
               <td>0.292% (38,463)</td>
            </tr>
            <tr>
               <td>Dark</td>
               <td>0.179% (23,575)</td>
            </tr>
            <tr>
               <td>Bright</td>
               <td>0.431% (56,754)</td>
            </tr>
            <tr>
               <td>Mislabels</td>
               <td>3.064% (402,963)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>14.581% (1,917,948)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/imagenet-21k/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://forms.gle/8jxPkyzeKj82kPed8">Request access here</a>
      </td>
      <td><code>from visuallayer.datasets.zoo import VLImageNet</code></td>
   </tr>
   <tr>
      <td><a href="./dataset_card/imagenet-1k/card.md">ImageNet-1K</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>0.57% (7,522)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.09% (1,199)</td>
            </tr>
            <tr>
               <td>Blur</td>
               <td>0.19% (2,478)</td>
            </tr>
            <tr>
               <td>Dark</td>
               <td>0.24% (3,174)</td>
            </tr>
            <tr>
               <td>Bright</td>
               <td>0.06% (770)</td>
            </tr>
            <tr>
               <td>Mislabels</td>
               <td>0.11% (1,480)</td>
            </tr>
            <tr>
               <td>Leakage</td>
               <td>0.065% (869)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>1.313% (17,492)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/imagenet-1k/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://forms.gle/8jxPkyzeKj82kPed8">Request access here</a>
      </td>
      <td><code>from visuallayer.datasets.zoo import VLImageNet</code></td>
   </tr>
   <tr>
      <td><a href="./dataset_card/food101/card.md">Food-101</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>0.23% (235)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.08% (77)</td>
            </tr>
            <tr>
               <td>Blur</td>
               <td>0.18% (185)</td>
            </tr>
            <tr>
               <td>Dark</td>
               <td>0.04% (43)</td>
            </tr>
            <tr>
               <td>Leakage</td>
               <td>0.086% (87)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>0.62% (627)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/food101/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://drive.google.com/uc?export=download&id=1ZG5GvU342l4YmSeYo6v6LeKbMM5fwjjw">Download here</a>
      </td>
      <td><code>from visuallayer.datasets.zoo import VLFood101</code></td>
   </tr>
   <tr>
      <td><a href="./dataset_card/oxford-iiit-pets/card.md">Oxford-IIIT Pet</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>1.016% (75)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.1% (7)</td>
            </tr>
            <tr>
               <td>Dark</td>
               <td>0.05% (4)</td>
            </tr>
            <tr>
               <td>Leakage</td>
               <td>0.31% (23)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>1.48% (132)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/oxford-iiit-pets/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://drive.google.com/uc?export=download&id=1OLa8k4NITnmCHjeByzvGaWt3W7k6R1QL">Download here</a>
      </td>
      <td><code>from visuallayer.datasets.zoo import VLOxfordIIITPet</code></td>
   </tr>
   <tr>
      <td><a href="./dataset_card/laion-1b/card.md">LAION-1B</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>WIP % (WIP)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>WIP % (WIP)</td>
            </tr>
            <tr>
               <td>Broken</td>
               <td>WIP % (WIP)</td>
            </tr>
            <tr>
               <td>Blur</td>
               <td>WIP % (WIP)</td>
            </tr>
            <tr>
               <td>Dark</td>
               <td>WIP % (WIP)</td>
            </tr>
            <tr>
               <td>Bright</td>
               <td>WIP % (WIP)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/laion-1b/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://forms.gle/8jxPkyzeKj82kPed8">Request access here</a>
      </td>
      <td>WIP</td>
   </tr>
   <tr>
      <td><a href="./dataset_card/kitti/card.md">KITTI</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>15.29% (2,294)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.01% (2)</td>
            </tr>
            <tr>
               <td>Leakage</td>
               <td>3.01% (452)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>18.32% (2,748)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/kitti/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://forms.gle/8jxPkyzeKj82kPed8">Request access here</a>
      </td>
      <td><code>from visuallayer.datasets.zoo import VLKitti</code></td>
   </tr>
   <tr>
      <td><a href="./dataset_card/deep-fashion/card.md">DeepFashion</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>5.11% (14,773)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.04% (108)</td>
            </tr>
            <tr>
               <td>Leakage</td>
               <td>2.75% (7,943)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>7.89% (22,824)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/deep-fashion/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://forms.gle/8jxPkyzeKj82kPed8">Request access here</a>
      </td>
      <td>WIP</td>
   </tr>
   <tr>
      <td><a href="./dataset_card/celeb-a-hq/card.md">CelebA-HQ</a></td>
      <td>
         <table>
            <tr>
               <td>Duplicates</td>
               <td>1.67% (3,389)</td>
            </tr>
            <tr>
               <td>Outliers</td>
               <td>0.08% (157)</td>
            </tr>
            <tr>
               <td>Blur</td>
               <td>0.51% (1,037)</td>
            </tr>
            <tr>
               <td>Dark</td>
               <td>0.001% (2)</td>
            </tr>
            <tr>
               <td>Mislabels</td>
               <td>0.01% (13)</td>
            </tr>
            <tr>
               <td>Leakage</td>
               <td>0.09% (188)</td>
            </tr>
            <tr>
               <td><strong>Total</strong></td>
               <td>2.362% (4,786)</td>
            </tr>
         </table>
         <div align="right">
            <a href="./dataset_card/celeb-a-hq/card.md"><strong>More »</strong></a>
         </div>
      </td>
      <td>
         <a href="https://forms.gle/8jxPkyzeKj82kPed8">Request access here</a>
      </td>
      <td>WIP</td>
   </tr>
</table> -->


Sign up to access our cloud platform [here](https://visual-layer.link).

<!-- > **NOTE**: Sign up [here](https://forms.gle/8jxPkyzeKj82kPed8) for free to be our beta testers and get full access to the all the `.csv` files for the dataset listed in this repo.  -->


## Installation

**Option 1** - Install `visuallayer` package from [PyPI](https://pypi.org/project/visuallayer/):

```shell
pip install visuallayer
```

**Option 2** - Install the bleeding edge version on GitHub:
```
pip install git+https://github.com/visual-layer/visuallayer.git@main --upgrade
```

## Usage

### Loading
To list all datasets supported by `visuallayer` run

```python
import visuallayer as vl
vl.datasets.zoo.list_datasets()
```

To load a dataset from the zoo:
```python
vl.datasets.zoo.load('vl-oxford-iiit-pets')
```

This loads the **clean version** of the Oxford IIIT Pets dataset where all of the problematic images are excluded from the dataset.

To load the original Oxford IIIT Pets dataset, specify the "original" argument:

```python
original_pets_dataset = vl.datasets.zoo.load('vl-oxford-iiit-pets', "original")
```

This loads the original dataset with no modifications.

### Inspecting
You can view the information about the dataset by calling 

```python
my_pets.info
```

which outputs the metadata of the dataset:

```shell
Metadata:
--> Name - vl-oxford-iiit-pets
--> Description - A modified version of the original Oxford IIIT Pets Dataset removing dataset issues.
--> License - Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
--> Homepage URL - https://www.robots.ox.ac.uk/~vgg/data/pets/
--> Number of Images - 7349
--> Number of Images with Issues - 109
```

To view the issues summary.

```python
my_pets.report
```

```shell
| Reason    | Count | Pct   |
|-----------|-------|-------|
| Duplicate | 75    | 1.016 |
| Outlier   | 7     | 0.095 |
| Dark      | 4     | 0.054 |
| Leakage   | 23    | 0.627 |
| Total     | 109   | 1.792 |

```

To explore and visualize the issues, run:

```python
my_pets.explore()
```
![explore](./imgs/explore.gif)

### Exporting
Export the dataset into PyTorch `Dataset` object with 

```python
test_dataset = my_pets.export(output_format="pytorch", split="test")
```

Now you can load the train and validation datasets in a PyTorch training loop. See the [Learn from Examples](#learn-from-examples) section to learn more.

Similarly you can also export the image and label into a `DataFrame`:

```python
test_dataframe = my_pets.export(output_format="csv", split="test")
```





## Learn from Examples

<table>
	<tr>
		<td rowspan="4" width="160">
			<a href="https://visual-layer.readme.io/docs/getting-started">
				<img src="./imgs/food.jpg" width="256" />
			</a>
		</td>
		<td rowspan="4">
			<ul>
				<li><b>Dataset:</b> <code>VLFood101</code></li>
				<li><b>Framework:</b> PyTorch.</li>
				<li><b>Description:</b> Load a dataset and train a PyTorch model.</li>
			</ul>
		</td>
		<td align="center" width="80">
			<a href="https://nbviewer.org/github/visual-layer/visuallayer/blob/main/notebooks/train-pytorch.ipynb">
				<img src="./imgs/nbviewer_logo.svg" height="34" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://github.com/visual-layer/visuallayer/blob/main/notebooks/train-pytorch.ipynb">
				<img src="./imgs/github_logo.png" height="32" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://colab.research.google.com/github/visual-layer/visuallayer/blob/main/notebooks/train-pytorch.ipynb">
				<img src="./imgs/colab_logo.png" height="28" />
			</a>
		</td>
	</tr>
    <tr>
		<td align="center">
			<a href="https://kaggle.com/kernels/welcome?src=https://github.com/visual-layer/visuallayer/blob/main/notebooks/train-pytorch.ipynb">
				<img src="./imgs/kaggle_logo.png" height="28" />
			</a>
		</td>
	</tr>
	<!-- ------------------------------------------------------------------- -->
	<tr>
		<td rowspan="4" width="160">
			<a href="https://visual-layer.readme.io/docs/objects-and-bounding-boxes">
				<img src="./imgs/pet.jpg" width="256" />
			</a>
		</td>
		<td rowspan="4">
			<ul>
				<li><b>Dataset:</b> <code>VLOxfordIIITPet</code></li>
				<li><b>Framework:</b> fast.ai.</li>
				<li><b>Description:</b> Finetune a pretrained TIMM model using fastai.</li>
			</ul>
		</td>
		<td align="center" width="80">
			<a href="https://nbviewer.org/github/visual-layer/visuallayer/blob/main/notebooks/train-fastai.ipynb">
				<img src="./imgs/nbviewer_logo.svg" height="34" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://github.com/visual-layer/visuallayer/blob/main/notebooks/train-fastai.ipynb">
				<img src="./imgs/github_logo.png" height="32" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://colab.research.google.com/github/visual-layer/visuallayer/blob/main/notebooks/train-fastai.ipynb">
				<img src="./imgs/colab_logo.png" height="28" />
			</a>
		</td>
	</tr>
    <tr>
		<td align="center">
			<a href="https://kaggle.com/kernels/welcome?src=https://github.com/visual-layer/visuallayer/blob/main/notebooks/train-fastai.ipynb">
				<img src="./imgs/kaggle_logo.png" height="28" />
			</a>
		</td>
	</tr>
	<!-- ------------------------------------------------------------------- -->
	<tr>
		<td rowspan="4" width="160">
			<a href="https://visual-layer.readme.io/docs/getting-started">
				<img src="./imgs/imagenet.jpg" width="256" />
			</a>
		</td>
		<td rowspan="4">
			<ul>
				<li><b>Dataset:</b> <code>VLImageNet</code></li>
				<li><b>Framework:</b> PyTorch.</li>
				<li><b>Description:</b> Load cleaned ImageNet dataset and train a PyTorch model.</li>
			</ul>
		</td>
		<td align="center" width="80">
			<a href="https://nbviewer.org/github/visual-layer/visuallayer/blob/main/notebooks/imagenet-1k-pytorch.ipynb">
				<img src="./imgs/nbviewer_logo.svg" height="34" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://github.com/visual-layer/visuallayer/blob/main/notebooks/imagenet-1k-pytorch.ipynb">
				<img src="./imgs/github_logo.png" height="32" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://colab.research.google.com/github/visual-layer/visuallayer/blob/main/notebooks/imagenet-1k-pytorch.ipynb">
				<img src="./imgs/colab_logo.png" height="28" />
			</a>
		</td>
	</tr>
    <tr>
		<td align="center">
			<a href="https://kaggle.com/kernels/welcome?src=https://github.com/visual-layer/visuallayer/blob/main/notebooks/train-pytorch.ipynb">
				<img src="./imgs/kaggle_logo.png" height="28" />
			</a>
		</td>
	</tr>
	
</table>


## License
`visuallayer` is licensed under the Apache 2.0 License. See [LICENSE](./LICENSE).

However, you are bound to the usage license of the original dataset. It is your responsibility to determine whether you have permission to use the dataset under the dataset's license. We provide no warranty or guarantee of accuracy or completeness.

## Usage Tracking

<details>
<summary>Disclaimer</summary>

This repository incorporates usage tracking using [Sentry.io](https://sentry.io/) to monitor and collect valuable information about the usage of the application.

Usage tracking allows us to gain insights into how the application is being used in real-world scenarios. It provides us with valuable information that helps in understanding user behavior, identifying potential issues, and making informed decisions to improve the application.

We DO NOT collect folder names, user names, image names, image content and other personaly identifiable information.

What data is tracked?
+ **Errors and Exceptions**: Sentry captures errors and exceptions that occur in the application, providing detailed stack traces and relevant information to help diagnose and fix issues.
+ **Performance Metrics**: Sentry collects performance metrics, such as response times, latency, and resource usage, enabling us to monitor and optimize the application's performance.

To opt out, define an environment variable named `SENTRY_OPT_OUT`. 

On Linux run the following:
```bash
export SENTRY_OPT_OUT=True
```

Read more on Sentry's official [webpage](https://sentry.io/welcome/).
</details>


## Getting Help
Get help from the Visual Layer team or community members via the following channels -
+ [Slack](https://visualdatabase.slack.com/join/shared_invite/zt-19jaydbjn-lNDEDkgvSI1QwbTXSY6dlA#/shared-invite/email).
+ GitHub [issues](https://github.com/visual-layer/visuallayer/issues).
+ Discussion [forum](https://visual-layer.readme.io/discuss).

## About Visual-Layer

<div align="center">
<a href="https://www.visual-layer.com">
  <img alt="Visual Layer Logo" src="https://raw.githubusercontent.com/visual-layer/fastdup/main/gallery/visual_layer_logo.png" alt="Logo" width="250">
</a>
</div>


Visual Layer is founded by the authors of [XGBoost](https://github.com/apache/tvm), [Apache TVM](https://github.com/apache/tvm) & [Turi Create](https://github.com/apple/turicreate) - [Danny Bickson](https://www.linkedin.com/in/dr-danny-bickson-835b32), [Carlos Guestrin](https://www.linkedin.com/in/carlos-guestrin-5352a869) and [Amir Alush](https://www.linkedin.com/in/amiralush).

Learn more about Visual Layer [here](https://visual-layer.com).