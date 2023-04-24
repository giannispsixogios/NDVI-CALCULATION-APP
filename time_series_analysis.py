# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:45:27 2023

@author: giannisps
"""

import gdal
import numpy as np
import matplotlib.pyplot as plt

# Define the paths to the input images
image_path_1 = r'C:\Users\GNR\Desktop\ΕΙΚΟΝΕΣ\1\EIKONA1.tif'
image_path_2 = r'C:\Users\GNR\Desktop\ΕΙΚΟΝΕΣ\2\EIKONA2.tif'

# Open the input images using the GDAL library
image_1 = gdal.Open(image_path_1)
image_2 = gdal.Open(image_path_2)

# Read the red and near-infrared bands from the input images
red_band_1 = image_1.GetRasterBand(4).ReadAsArray().astype(np.float32)
nir_band_1 = image_1.GetRasterBand(5).ReadAsArray().astype(np.float32)
red_band_2 = image_2.GetRasterBand(4).ReadAsArray().astype(np.float32)
nir_band_2 = image_2.GetRasterBand(5).ReadAsArray().astype(np.float32)

# Calculate the NDVI values for both images
ndvi_1 = (nir_band_1 - red_band_1) / (nir_band_1 + red_band_1)
ndvi_2 = (nir_band_2 - red_band_2) / (nir_band_2 + red_band_2)

# Calculate the difference in NDVI values between the two images
ndvi_diff = ndvi_2 - ndvi_1

plt.imshow(ndvi_diff)
plt.show()


# Print the mean and standard deviation of the NDVI difference
print('Mean NDVI difference:', np.mean(ndvi_diff))
print('Standard deviation of NDVI difference:', np.std(ndvi_diff))