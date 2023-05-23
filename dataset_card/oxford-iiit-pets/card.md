# Dataset Card - Oxford IIIT Pets
![datasetimage](https://www.robots.ox.ac.uk/~vgg/data/pets/pet_annotations.jpg)

+ Home page - https://www.robots.ox.ac.uk/~vgg/data/pets/

+ Paper - https://www.robots.ox.ac.uk/~vgg/publications/2012/parkhi12a/parkhi12a.pdf

+ License - [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

+ Total images in dataset - 7349.

## Summary

The Oxford-IIIT pet dataset comprises 37 categories of pet images, with approximately 200 images per class. The dataset exhibits significant variations in scale, pose, and lighting. Each image is accompanied by a ground truth annotation indicating the breed.


## Issues Found
Here are some of the issues found.

+ Duplicates - 1.021% (75)
+ Outliers - 0.095% (7)
+ Dark - 0.054% (4)

Total problematic images - 1.17% (86 out of 7349)

### 1. Duplicates
![duplicate](./duplicates.png)

### 2. Outliers
![outliers](./outliers.png)

### 3. Dark
![dark](./dark.png)