# Dataset Card - Food101
![datasetimage](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/static/img/food-101.jpg)

+ Home page - https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/

+ Paper - https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/static/bossard_eccv14_food-101.pdf

+ License - Unknown.

+ Total images in dataset - 101,000.

## Summary

A challenging data set of 101 food categories is introduced, consisting of 101,000 images. Each class includes 250 manually reviewed test images and 750 training images. The training images deliberately retain some noise, primarily intense colors and occasional incorrect labels. All images have been rescaled to a maximum side length of 512 pixels.


## Issues Found
Here are some of the issues found:
<ol>
<li>Duplicates - 0.23% (235)</li>
<li>Outliers - 0.08% (77)</li>
<li>Blur - Blur - 0.18% (185)</li>
<li>Dark - 0.04% (43)</li>
<li>Leakage - 0.35% (87)</li>
<li><b>Total</b> - 0.88% (627)</li>
</ol>

![issues](food.gif)

### 1. Duplicates
![duplicate](./duplicates.png)

### 2. Outliers
![outliers](./outliers.png)

### 3. Blur
![dark](./blur.png)

### 4. Dark
![dark](./dark.png)

