# Dataset Card - ImageNet-1K
![image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F58%2F0a%2F99%2F580a99345134d954ed2cfe8ea7ccf55a.jpg&f=1&nofb=1&ipt=1a4e152e0b8a36e2da4e0f1a0e020d6857761391be9aec95ac7f5c502966dc01&ipo=images)

+ Home page - https://www.image-net.org/

+ Paper - https://arxiv.org/abs/1409.0575

+ License - Unknown.

+ Total images in dataset - 1,431,167.


## Summary
This dataset provides access to the most commonly used subset of ImageNet, with 1000 object classes, 1,281,167 training images, 50,000 validation images, and 100,000 test images. It includes a patch for corrupted test set images. For the full ImageNet dataset, visit the download section of the main website.


## Issues Found
Here are some of the issues found.

+ Duplicates - 0.565 % (7,522)
+ Outliers - 0.090 % (1,199)
+ Blur - 0.186 % (2,478)
+ Dark - 0.238 % (3,174)
+ Bright - 0.058 % (770)
+ Mislabels - 0.111 % (1,480)
+ Data Leakage - 1.738 % (869)
+ **Total** - 2.986 % (17,492 of 1,431,167)

### 1. Duplicates
![duplicates](./duplicates.png)

### 2. Outliers
![outliers](./outliers.png)

### 3. Blur
![blur](./blur.png)

### 4. Dark
![dark](./dark.png)

### 5. Bright
![brigth](./bright.png)

### 6. Mislabels
![mislabels](./mislabels.png)

### 7. Leakage
