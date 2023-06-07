# Dataset Card - Common Object in Context (COCO)
<img src="https://cocodataset.org/images/coco-examples.jpg" height="200" />

+ Home page - https://cocodataset.org/#home

+ Paper - https://arxiv.org/abs/1405.0312

+ License - [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

+ Total images in dataset - 328,000.

## Summary
The COCO dataset is a large-scale object detection, segmentation, and captioning dataset. It is widely used in computer vision research and has been used to train and evaluate many state-of-the-art object detection and segmentation models.
The COCO dataset contains over 330,000 images, each annotated with 80 object categories and 5 captions describing the scene. The dataset has two main parts: the images and their annotations.

## Issues Found
Here are some of the issues found in each dataset split.

Overall:
| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 201       | 0.123       |
| **Dark**      | 174       | 0.106       |
| **Outlier**   | 143       | 0.087       |
| **Blur**      | 47        | 0.029       |
| **Bright**    | 21        | 0.013       |
| **Leakage**   | 20        | 0.012       |
| **TOTAL**     | 606       | 0.37        |

Train Split:
| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 140       | 0.085       |
| **Dark**      | 125       | 0.076       |
| **Outlier**   | 93        | 0.057       |
| **Blur**      | 33        | 0.02        |
| **Bright**    | 16        | 0.01        |
| **Leakage**   | 17        | 0.01        |
| **TOTAL**     | 424       | 0.258       |

Validation Split:
| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 11        | 0.007       |
| **Outlier**   | 7         | 0.004       |
| **Dark**      | 4         | 0.002       |
| **Blur**      | 2         | 0.001       |
| **Bright**    | 1         | 0.001       |
| **Leakage**   | 3         | 0.002       |
| **TOTAL**     | 28        | 0.017       |

Test Split:
| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 50        | 0.03        |
| **Dark**      | 45        | 0.027       |
| **Outlier**   | 43        | 0.026       |
| **Blur**      | 12        | 0.007       |
| **Bright**    | 4         | 0.002       |
| **TOTAL**     | 154       | 0.092       |


### 1. Duplicates

### 2. Outliers

### 3. Blur

### 4. Dark

### 5. Bright
