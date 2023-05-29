# Dataset Card - Food101
![datasetimage](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/static/img/food-101.jpg)

+ Home page - https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/

+ Paper - https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/static/bossard_eccv14_food-101.pdf

+ License - Unknown.

+ Total images in dataset - 101,000.

## Summary

A challenging data set of 101 food categories is introduced, consisting of 101,000 images. Each class includes 250 manually reviewed test images and 750 training images. The training images deliberately retain some noise, primarily intense colors and occasional incorrect labels. All images have been rescaled to a maximum side length of 512 pixels.


## Issues Found
Here are some of the issues found.

+ Duplicates - 0.233 % (235)
+ Outliers - 0.076 % (77)
+ Blur - 0.183 % (185)
+ Dark - 0.043 % (43)

Total problematic images - 0.535% (540 out of 101,000)

![issues](food.gif)

### 1. Duplicates
![duplicate](./duplicates.png)

### 2. Outliers
![outliers](./outliers.png)

### 3. Blur
![dark](./blur.png)

### 4. Dark
![dark](./dark.png)

