# Dataset Card - Oxford IIIT Pets
<img src="https://www.robots.ox.ac.uk/~vgg/data/pets/pet_annotations.jpg" height="200" />

+ Home page - https://www.robots.ox.ac.uk/~vgg/data/pets/

+ Paper - https://www.robots.ox.ac.uk/~vgg/publications/2012/parkhi12a/parkhi12a.pdf

+ License - [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

+ Total images in dataset - 7349.

## Summary

The Oxford-IIIT pet dataset comprises 37 categories of pet images, with approximately 200 images per class. The dataset exhibits significant variations in scale, pose, and lighting. Each image is accompanied by a ground truth annotation indicating the breed.


## Issues Found
Here are some of the issues found in each dataset split.

Overall:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 75        | 1.016       |
| **Outlier**   | 7         | 0.095       |
| **Dark**      | 4         | 0.054       |
| **Leakage**   | 23        |             |
| **TOTAL**     | 109       | 1.165       |


Train Split:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 14        | 0.19        |
| **Outlier**   | 4         | 0.054       |
| **Dark**      | 3         | 0.041       |
| **TOTAL**     | 21        | 0.285       |


Test Split:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 29        | 0.393       |
| **Outlier**   | 3         | 0.041       |
| **Dark**      | 1         | 0.014       |
| **Leakage**   | 23        | 0.627       |
| **Total**     | 33        | 0.448       |

Unannotated:

| **Reason**    | **Count** | **Percent** |
|---------------|-----------|-------------|
| **Duplicate** | 32        | 0.433       |
| **Total**     | 32        | 0.433       |

### 1. Duplicates
![duplicate](./duplicates.png)

### 2. Outliers
![outliers](./outliers.png)

### 3. Dark
![dark](./dark.png)