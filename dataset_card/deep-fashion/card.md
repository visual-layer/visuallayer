# Dataset Card - DeepFashion
![image](https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion/intro.jpg)

+ Home page - http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html

+ Paper - https://ieeexplore.ieee.org/document/7780493

+ License - Non-commmercial and research purposes only.

+ Total images in dataset - 800,000.

## Summary
DeepFashion is a large-scale clothes database with comprehensive annotations. It contains over 800,000 images, which are richly annotated with massive attributes, clothing landmarks, and correspondence of images taken under different scenarios including store, street snapshot, and consumer.

## Issues Found
Here are some of the issues found in each dataset split.

Overall:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 14773     | 5.108       |
| **Outlier**   | 108       | 0.037       |
| **Leakage**   | 7943      | 19.858      |
| **TOTAL**     | 22824     | 25.003      |

Train Split:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 10696     | 3.698       |
| **Outlier**   | 74        | 0.026       |
| **TOTAL**     | 10770     | 3.724       |

Validation Split:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 2089      | 0.722       |
| **Outlier**   | 14        | 0.005       |
| **Leakage**   | 3717      | 9.293       |
| **TOTAL**     | 5820      | 10.02       |


Test Split:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 1988      | 0.687       |
| **Outlier**   | 20        | 0.007       |
| **Leakage**   | 4226      | 10.565      |
| **TOTAL**     | 6234      | 11.259      |


### 1. Duplicates


### 2. Outliers
