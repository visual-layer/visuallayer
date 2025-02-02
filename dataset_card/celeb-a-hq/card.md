# Dataset Card - CelebA-HQ
<img src="https://pythonawesome.com/content/images/2018/07/celebA-HQ.jpg" height="200" />


+ Home page - https://github.com/tkarras/progressive_growing_of_gans

+ Paper - https://openreview.net/pdf?id=Hk99zCeAb

+ License - [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

+ Total images in dataset - 30,000.

## Summary
The CelebA-HQ dataset is a high-quality version of the CelebA dataset that consists of 30,000 images at 1024×1024 resolution. The images are aligned and cropped to the face region, and they have been carefully selected to be of high quality. The dataset is also accompanied by a variety of annotations, including facial landmarks, facial attributes, and binary masks.

## Issues Found
Here are some of the issues found in each dataset split.

Overall:
| **Reason**     | **Count** | **Percent** |
|----------------|-----------|-------------|
| **Duplicate**  | 3389      | 1.673       |
| **Blur**       | 1037      | 0.512       |
| **Outlier**    | 157       | 0.077       |
| **Dark**       | 2         | 0.001       |
| **Mislabeled** | 13        | 0.006       |
| **Leakage**    | 188       | 0.093       |
| **TOTAL**      | 4786      | 2.362       |

Train Split:
| **Reason**     | **Count** | **Percent** |
|----------------|-----------|-------------|
| **Duplicate**  | 2618      | 1.292       |
| **Blur**       | 849       | 0.419       |
| **Outlier**    | 132       | 0.065       |
| **Dark**       | 2         | 0.001       |
| **Mislabeled** | 10        | 0.005       |
| **Leakage**    | 180       | 0.089       |
| **TOTAL**      | 3791      | 1.871       |


Validation Split:
| **Reason**     | **Count** | **Percent** |
|----------------|-----------|-------------|
| **Duplicate**  | 390       | 0.192       |
| **Blur**       | 96        | 0.047       |
| **Outlier**    | 18        | 0.009       |
| **Mislabeled** | 2         | 0.001       |
| **Leakage**    | 8         | 0.004       |
| **TOTAL**      | 514       | 0.253       |

Test Split:
| **Reason**     | **Count** | **Percent** |
|----------------|-----------|-------------|
| **Duplicate**  | 381       | 0.188       |
| **Blur**       | 92        | 0.045       |
| **Outlier**    | 7         | 0.003       |
| **Mislabeled** | 1         | 0           |
| **TOTAL**      | 481       | 0.236       |


### 1. Duplicates


### 2. Outliers


### 3. Dark
