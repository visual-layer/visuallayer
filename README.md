
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
<h3 align="center">Simplify Your Visual Data Ops</h3>
  <p align="center">
  <br />
    <a href="https://docs.visual-layer.com/docs/getting-started" target="_blank" rel="noopener noreferrer"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/visual-layer/visuallayer/issues" target="_blank" rel="noopener noreferrer">Report Issues</a>
    ·
    <a href="https://medium.com/visual-layer/" target="_blank" rel="noopener noreferrer">Read Blog</a>
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
`visuallayer` is a pure Python and open-source package that offers access and extensibility to the [cloud version](https://app.visual-layer.com) of the Visual Layer platform capabilities from your code. 

While the cloud version offers a high-level overview and visualization of your data, the SDK affords you the flexibility to integrate into your favorite machine learning frameworks and environments (e.g. Jupyter Notebook) using Python.

## Installation

The easiest way to use the `visuallayer` SDK is to install it from PyPI. On your machine, run:

```shell
pip install visuallayer
```

Optionally, you can also install the bleeding edge version on [GitHub](https://github.com/visual-layer/visuallayer) by running:

```shell
pip install git+https://github.com/visual-layer/visuallayer.git@main --upgrade
```

## VL-Datasets
The `visuallayer` package also lets you access [VL-Datasets](https://docs.visual-layer.com/docs/what-are-vl-datasets) - a collection of sanitized version of widely used computer vision datasets.


For example, with only 2 lines of code, load the sanitized version of the [ImageNet-1k](https://www.robots.ox.ac.uk/~vgg/data/pets/) dataset with:

![image](./imgs/usage.png)

> **Note**: `visuallayer` does not automatically download the ImageNet dataset, you should make sure to obtain usage rights to the dataset and download it into your current working directory first.

When we say "sanitized", we mean that the datasets loaded by `visuallayer` are free from common issues such as:

+ Duplicates.
+ Near Duplicates.
+ Broken images.
+ Outliers.
+ Dark/Bright/Blurry images.
+ Mislabels.
+ Data Leakage.

![image](./imgs/issues.png)






## Dataset Zoo
We provide a [Dataset Zoo](https://docs.visual-layer.com/docs/available-datasets) where you can find all information for each VL-Dataset.

For each dataset in the zoo, we ran an analyis using our cloud platform and found issues pertaining to the dataset. They are all summarized in the tables below. You can also download the issues found for free.


<table>
    <thead>
        <tr>
            <th align="left">VL Dataset</th>
            <th align="left">Original Dataset</th>
            <th align="left">Total Images</th>
            <th align="left">Total Issues (%)</th>
            <th align="left">Total Issues (Count)</th>
            <th align="left">Issues CSV</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="left"><a href="#vl-imagenet-21k">vl-imagenet-21k</a></td>
            <td align="left">ImageNet-21K</td>
            <td align="left"><div align="left">13,153,500</td>
            <td align="left"><div align="left">14.58%</td>
            <td aalign="left"><div align="left">1,917,948</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-21K_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#vl-imagenet-1k">vl-imagenet-1k</a></td>
            <td align="left">ImageNet-1K</td>
            <td align="left"><div align="left">1,431,167</td>
            <td aalign="left"><div align="left">1.31%</td>
            <td align="left"><div align="left">17,492</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-1K_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#laion-2b">vl-laion-1b</a></td>
            <td align="left">LAION-1B</td>
            <td align="left"><div align="left">1,000,000,000</td>
            <td align="left"><div align="left">10.40%</td>
            <td align="left"><div align="left">104,942,474</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Laion1B_issues.parquet"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#kitti">vl-kitti</a></td>
            <td align="left">KITTI</td>
            <td align="left"><div align="left">12,919</td>
            <td align="left"><div align="left">18.32%</td>
            <td align="left"><div align="left">2,748</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Kitti_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#coco">vl-coco</a></td>
            <td align="left">COCO</td>
            <td align="left"><div align="left">330,000</td>
            <td align="left"><div align="left">0.31%</td>
            <td align="left"><div align="left">508</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Coco_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#deepfashion">vl-deepfashion</a></td>
            <td align="left">DeepFashion</td>
            <td align="left"><div align="left">800,000</td>
            <td align="left"><div align="left">7.89%</td>
            <td align="left"><div align="left">22,824</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/DeepFashion_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#celeba-hq">vl-celeba-hq</a></td>
            <td align="left">CelebA-HQ</td>
            <td align="left"><div align="left">30,000</td>
            <td align="left"><div align="left">2.36%</td>
            <td align="left"><div align="left">4,786</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/CelebA_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#places365">vl-places365</a></td>
            <td align="left">Places365</td>
            <td align="left"><div align="left">1,800,000</td>
            <td align="left"><div align="left">2.09%</td>
            <td align="left"><div align="left">37,644</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Places365_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#food-101">vl-food-101</a></td>
            <td align="left">Food-101</td>
            <td align="left"><div align="left">101,000</td>
            <td align="left"><div align="left">0.62%</td>
            <td align="left"><div align="left">627</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
        <tr>
            <td align="left"><a href="#oxford-iiit-pet">vl-oxford-iiit-pet</a></td>
            <td align="left">Oxford-IIIT Pet</td>
            <td align="left"><div align="left">7,349</td>
            <td align="left"><div align="left">1.48%</td>
            <td align="left"><div align="left">132</td>
            <td align="left"><a href="https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_file_list.csv"><img src="https://img.shields.io/badge/Download-Click%20Here-brightgreen.svg?style=for-the-badge" alt="download"></a></td>
        </tr>
    </tbody>
</table>


The sanitized version of a dataset is prefixed with `vl-` to differentiate it from the original dataset.




<!-- | Dataset Name    | Total Images  | Total Issues (%) | Total Issues (Count) | Duplicates (%) | Duplicates (Count) | Outliers (%) | Outliers (Count) | Blur (%) | Blur (Count) | Dark (%) | Dark (Count) | Bright (%) | Bright (Count) | Mislabels (%) | Mislabels (Count) | Leakage (%) | Leakage (Count) |
|-----------------|---------------|------------------|----------------------|----------------|--------------------|--------------|------------------|----------|--------------|----------|--------------|------------|----------------|---------------|-------------------|-------------|-----------------|
| ImageNet-21K    | 13,153,500    | 14.58%           | 1,917,948            | 10.53%         | 1,385,074          | 0.09%        | 11,119           | 0.29%    | 38,463       | 0.18%    | 23,575       | 0.43%      | 56,754         | 3.06%         | 402,963           | -           | -               |
| ImageNet-1K     | 1,431,167     | 1.31%            | 17,492               | 0.57%          | 7,522              | 0.09%        | 1,199            | 0.19%    | 2,478        | 0.24%    | 3,174        | 0.06%      | 770            | 0.11%         | 1,480             | 0.07%       | 869             |
| LAION-1B        | 2,000,000,000 | 10.40%           | 104,942,474          | 8.89%          | 89,349,899         | 0.63%        | 6,350,368        | 0.77%    | 7,763,266    | 0.02%    | 242,333      | 0.12%      | 1,236,608      | -             | -                 | -           | -               |
| KITTI           | 12,919        | 18.32%           | 2,748                | 15.29%         | 2,294              | 0.01%        | 2                | -        | -            | -        | -            | -          | -              | -             | -                 | 3.01%       | 452             |
| COCO            | 330,000       | 0.31%            | 508                  | 0.12%          | 201                | 0.09%        | 143              | 0.03%    | 47           | 0.05%    | 76           | 0.01%      | 21             | -             | -                 | 0.01%       | 20              |
| DeepFashion     | 800,000       | 7.89%            | 22,824               | 5.11%          | 14,773             | 0.04%        | 108              | -        | -            | -        | -            | -          | -              | -             | -                 | 2.75%       | 7,943           |
| CelebA-HQ       | 30,000        | 2.36%            | 4,786                | 1.67%          | 3,389              | 0.08%        | 157              | 0.51%    | 1,037        | 0.00%    | 2            | 0.01%      | 13             | -             | -                 | 0.09%       | 188             |
| Places365       | 1,800,000     | 2.09%            | 37,644               | 1.53%          | 27,520             | 0.40%        | 7,168            | -        | -            | 0.16%    | 2,956        | -          | -              | -             | -                 | -           | -               |
| Food-101        | 101,000       | 0.62%            | 627                  | 0.23%          | 235                | 0.08%        | 77               | 0.18%    | 185          | 0.04%    | 43           | -          | -              | -             | -                 | -           | -               |
| Oxford-IIIT Pet | 7,349         | 1.48%            | 132                  | 1.01%          | 75                 | 0.10%        | 7                | -        | -            | 0.05%    | 4            | -          | -              | -             | -                 | 0.31%       | 23              |
 -->

The following table is a detailed breakdown on the issues for each dataset.

<table>
    <tr>
      <th><strong>Dataset Name</strong></th>
      <td><strong>Total Images</strong></td>
      <td><strong>Total Issues (%)</strong></td>
      <td><strong>Total Issues (Count)</strong></td>
      <td><strong>Duplicates (%)</strong></td>
      <td><strong>Duplicates (Count)</strong></td>
      <td><strong>Outliers (%)</strong></td>
      <td><strong>Outliers (Count)</strong></td>
      <td><strong>Blur (%)</strong></td>
      <td><strong>Blur (Count)</strong></td>
      <td><strong>Dark (%)</strong></td>
      <td><strong>Dark (Count)</strong></td>
      <td><strong>Bright (%)</strong></td>
      <td><strong>Bright (Count)</strong></td>
      <td><strong>Mislabels (%)</strong></td>
      <td><strong>Mislabels (Count)</strong></td>
      <td><strong>Leakage (%)</strong></td>
      <td><strong>Leakage (Count)</strong></td>
      </tr>
    <tr>
        <th>ImageNet-21K</th>
         <td><div align="right">13,153,500</div></td>
         <td><div align="right">14.58%</div></td>
         <td><div align="right">1,917,948</div></td>
         <td><div align="right">10.53%</div></td>
         <td><div align="right">1,385,074</div></td>
         <td><div align="right">0.09%</div></td>
         <td><div align="right">11,119</div></td>
         <td><div align="right">0.29%</div></td>
         <td><div align="right">38,463</div></td>
         <td><div align="right">0.18%</div></td>
         <td><div align="right">23,575</div></td>
         <td><div align="right">0.43%</div></td>
         <td><div align="right">56,754</div></td>
         <td><div align="right">3.06%</div></td>
         <td><div align="right">402,963</div></td>
         <td><div align="right">-</div></td>
         <td><div align="right">-</div></td>
    </tr>
    <tr>
        <th>ImageNet-1K</th>
        <td><div align="right">1,431,167</td>
        <td><div align="right">1.31%</td>
        <td><div align="right">17,492</td>
        <td><div align="right">0.57%</td>
        <td><div align="right">7,522</td>
        <td><div align="right">0.09%</td>
        <td><div align="right">1,199</td>
        <td><div align="right">0.19%</td>
        <td><div align="right">2,478</td>
        <td><div align="right">0.24%</td>
        <td><div align="right">3,174</td>
        <td><div align="right">0.06%</td>
        <td><div align="right">770</td>
        <td><div align="right">0.11%</td>
        <td><div align="right">1,480</td>
        <td><div align="right">0.07%</td>
        <td><div align="right">869</td>
    </tr>
    <tr>
        <th>LAION-1B</th>
        <td><div align="right">1,000,000,000</td>
        <td><div align="right">10.40%</td>
        <td><div align="right">104,942,474</td>
        <td><div align="right">8.89%</td>
        <td><div align="right">89,349,899</td>
        <td><div align="right">0.63%</td>
        <td><div align="right">6,350,368</td>
        <td><div align="right">0.77%</td>
        <td><div align="right">7,763,266</td>
        <td><div align="right">0.02%</td>
        <td><div align="right">242,333</td>
        <td><div align="right">0.12%</td>
        <td><div align="right">1,236,608</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
    </tr>
    <tr>
        <th>KITTI</th>
        <td><div align="right">12,919</td>
        <td><div align="right">18.32%</td>
        <td><div align="right">2,748</td>
        <td><div align="right">15.29%</td>
        <td><div align="right">2,294</td>
        <td><div align="right">0.01%</td>
        <td><div align="right">2</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">3.01%</td>
        <td><div align="right">452</td>
    </tr>
    <tr>
        <th>COCO</th>
        <td><div align="right">330,000</td>
        <td><div align="right">0.31%</td>
        <td><div align="right">508</td>
        <td><div align="right">0.12%</td>
        <td><div align="right">201</td>
        <td><div align="right">0.09%</td>
        <td><div align="right">143</td>
        <td><div align="right">0.03%</td>
        <td><div align="right">47</td>
        <td><div align="right">0.05%</td>
        <td><div align="right">76</td>
        <td><div align="right">0.01%</td>
        <td><div align="right">21</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">0.01%</td>
        <td><div align="right">20</td>
    </tr>
    <tr>
        <th>DeepFashion</th>
        <td><div align="right">800,000</td>
        <td><div align="right">7.89%</td>
        <td><div align="right">22,824</td>
        <td><div align="right">5.11%</td>
        <td><div align="right">14,773</td>
        <td><div align="right">0.04%</td>
        <td><div align="right">108</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">2.75%</td>
        <td><div align="right">7,943</td>
    </tr>
    <tr>
        <th>CelebA-HQ</th>
        <td><div align="right">30,000</td>
        <td><div align="right">2.36%</td>
        <td><div align="right">4,786</td>
        <td><div align="right">1.67%</td>
        <td><div align="right">3,389</td>
        <td><div align="right">0.08%</td>
        <td><div align="right">157</td>
        <td><div align="right">0.51%</td>
        <td><div align="right">1,037</td>
        <td><div align="right">0.00%</td>
        <td><div align="right">2</td>
        <td><div align="right">0.01%</td>
        <td><div align="right">13</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">0.09%</td>
        <td><div align="right">188</td>
    </tr>
    <tr>
        <th>Places365</th>
        <td><div align="right">1,800,000</td>
        <td><div align="right">2.09%</td>
        <td><div align="right">37,644</td>
        <td><div align="right">1.53%</td>
        <td><div align="right">27,520</td>
        <td><div align="right">0.40%</td>
        <td><div align="right">7,168</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">0.16%</td>
        <td><div align="right">2,956</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
    </tr>
    <tr>
        <th>Food-101</th>
        <td><div align="right">101,000</td>
        <td><div align="right">0.62%</td>
        <td><div align="right">627</td>
        <td><div align="right">0.23%</td>
        <td><div align="right">235</td>
        <td><div align="right">0.08%</td>
        <td><div align="right">77</td>
        <td><div align="right">0.18%</td>
        <td><div align="right">185</td>
        <td><div align="right">0.04%</td>
        <td><div align="right">43</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
    </tr>
    <tr>
        <th>Oxford-IIIT Pet</th>
        <td><div align="right">7,349</td>
        <td><div align="right">1.48%</td>
        <td><div align="right">132</td>
        <td><div align="right">1.01%</td>
        <td><div align="right">75</td>
        <td><div align="right">0.10%</td>
        <td><div align="right">7</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">0.05%</td>
        <td><div align="right">4</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">-</td>
        <td><div align="right">0.31%</td>
        <td><div align="right">23</td>
    </tr>
</table>


We will continue to support more datasets. Here are a few currently in our roadmap:
+ EuroSAT
+ Flickr30k
+ INaturalist
+ SVHN
+ Cityscapes

[Let us know](https://forms.gle/8jxPkyzeKj82kPed8) if you have additional request to support a specific dataset.

> **Note**: If you'd like to use our cloud tool and discover issues with your own dataset, [sign up](https://app.visual-layer.com/) to use our cloud platform for free. 





<!-- 
## Access
The `visuallayer` SDK provides a convenient way to access the sanitized version of the datasets in Python.
Alternatively, for each dataset in this repo, we provide a `.csv` file that lists the problematic images from the dataset.

You can use the listed images in the `.csv` to improve the model by re-labeling them or just simply removing it from the dataset.

Here is a table of datasets, link to download the `.csv` file, and how to access it via `visuallayer` datasets zoo.

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
[laion-1b-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Laion1B_issues.parquet
[kitti-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Kitti_images_issue_file_list.csv
[coco-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Coco_images_issue_file_list.csv
[deepfashion-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/DeepFashion_images_issue_file_list.csv
[celeba-hq-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/CelebA_images_issue_file_list.csv
[places365-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Places365_images_issue_file_list.csv
[food101-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_file_list.csv
[oxford-pets-url]: https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_file_list.csv


We offer extensive visualizations of the dataset issues in our cloud platform.
[Sign up]((https://app.visual-layer.com)) for free. -->

## Usage
The following sections show how to use the `visuallayer` SDK to load, inspect and export a VL-Dataset.

### Loading a dataset
We offer handy functions to load datasets from the Dataset zoo.
First, let's list the datasets in the zoo with:


```python
import visuallayer as vl
vl.datasets.zoo.list_datasets()
```

which currently outputs:

```shell
['vl-oxford-iiit-pets',
 'vl-imagenet-21k',
 'vl-imagenet-1k',
 'vl-food101',
 'oxford-iiit-pets',
 'imagenet-21k',
 'imagenet-1k',
 'food101']
```

To load the dataset:

```python
vl.datasets.zoo.load('vl-oxford-iiit-pets')
```

This loads the sanitized version of the Oxford IIIT Pets dataset where all of the problematic images are excluded from the dataset.

To load the original Oxford IIIT Pets dataset, simply drop the `vl-` prefix:

```python
original_pets_dataset = vl.datasets.zoo.load('oxford-iiit-pets')
```

This loads the original dataset with no modifications.

### Inspecting a dataset
Now that you have a dataset loaded, you can view information pertaining to that dataset with:

```python
my_pets.info
```

This prints out high-level information about the original Dataset. In this example, we used the Pets Dataset from Oxford.

```shell
Metadata:
--> Name - vl-oxford-iiit-pets
--> Description - A modified version of the original Oxford IIIT Pets Dataset removing dataset issues.
--> License - Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
--> Homepage URL - https://www.robots.ox.ac.uk/~vgg/data/pets/
--> Number of Images - 7349
--> Number of Images with Issues - 109
```

If you'd like to view the issues related to the dataset, run:

```python
my_pets.report
```

which outputs:

```shell
| Reason    | Count | Pct   |
|-----------|-------|-------|
| Duplicate | 75    | 1.016 |
| Outlier   | 7     | 0.095 |
| Dark      | 4     | 0.054 |
| Leakage   | 23    | 0.627 |
| Total     | 109   | 1.792 |

```

Now that you've seen the issues with the dataset, you can visualize them on screen. There are two options to visualize the dataset issues.

> **Option 1** - Using the Visual Layer Cloud Platform - Provides an extensive capability to view, group, sort, and filter the dataset issues. Sign up for free.

> **Option 2** - In Jupyter notebook - Provides a limited but convenient way to view the dataset without leaving your notebook.

In this example, let's see how you can visualize the issues using **Option 2** in your notebook.

To do so, run:
```python
my_pets.explore()
```

This should output an interactive table in your Jupyter notebook like the following.

![explore](./imgs/explore.gif)

In the interactive table, you can view the issues, sort, filter, search, and compare the images side by side.

By default the .explore() load the top 50 issues from the dataset covering all issue types. If you'd like a more granular control, you can change the `num_images` and `issue` argument.

For example:

```python
pets_dataset.explore(num_images=100, issue='Duplicate')
```

The interactive table provides a convenient but limited way to visualize dataset issues.
For a more extensive visualization, view the issues using the Visual Layer Cloud Platform. Sign up for free.


### Exporting a dataset
If you'd like to use a loaded dataset to train a model, you can conveniently export the dataset with:

```python
test_dataset = my_pets.export(output_format="pytorch", split="test")
```
This exports the Dataset into a Pytorch `Dataset` object that can be used readily with a PyTorch training loop.

Alternatively, you can export the Dataset to a DataFrame with:

```python
test_dataset = pets_dataset.export(output_format="csv", split="test")
```


## Learn from Examples
In this section, we show an end-to-end example of how to load, inspect and export a dataset and then train using PyTorch and fastai framework.

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

## Telemetry

<details>
<summary>Usage Tracking</summary>

This repository incorporates usage tracking using [Sentry.io](https://sentry.io) to monitor and collect valuable information about the usage of the application.

Usage tracking allows us to gain insights into how the application is being used in real-world scenarios. It provides us with valuable information that helps in understanding user behavior, identifying potential issues, and making informed decisions to improve the application.

We DO NOT collect folder names, user names, image names, image content, and other personally identifiable information.

**What data is tracked?**

- Errors and Exceptions: Sentry captures errors and exceptions that occur in the application, providing detailed stack traces and relevant information to help diagnose and fix issues.
- Performance Metrics: Sentry collects performance metrics, such as response times, latency, and resource usage, enabling us to monitor and optimize the application's performance.

To opt-out, define an environment variable named `SENTRY_OPT_OUT`.

On Linux/macOS, run the following:
```shell
export SENTRY_OPT_OUT=True
```

Read more on [Sentry's official webpage](https://sentry.io).

</details>

<!-- This repository incorporates usage tracking using [Sentry.io](https://sentry.io/) to monitor and collect valuable information about the usage of the application.

Usage tracking allows us to gain insights into how the application is being used in real-world scenarios. It provides us with valuable information that helps in understanding user behavior, identifying potential issues, and making informed decisions to improve the application.

We DO NOT collect folder names, user names, image names, image content, and other personally identifiable information.

What data is tracked?
+ **Errors and Exceptions**: Sentry captures errors and exceptions that occur in the application, providing detailed stack traces and relevant information to help diagnose and fix issues.
+ **Performance Metrics**: Sentry collects performance metrics, such as response times, latency, and resource usage, enabling us to monitor and optimize the application's performance.

To opt-out, define an environment variable named `SENTRY_OPT_OUT`. 

On Linux run the following:
```bash
export SENTRY_OPT_OUT=True
```

Read more on Sentry's official [webpage](https://sentry.io/welcome/). -->


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