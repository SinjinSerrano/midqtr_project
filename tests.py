import cv2
import numpy as np
from midqtr_project import (
    RGBImage,
    ImageProcessing as IP
)

#Sample pixel matrix to test the different methods
pixels = [
[
    [100, 200, 150, 20],
    [30, 50, 60, 10],
    [123, 45, 123, 32],
],
[
    [50, 30, 140, 120],
    [90, 90, 87, 123],
    [56, 76, 34, 1],
],
[
    [40, 50, 120, 111],
    [150, 222, 12, 45],
    [10, 20, 30, 40],
],
]
test = RGBImage(pixels)
print(test.get_pixels())
negated = IP.negate(test)
print(negated.get_pixels())
print('\n' + str(test.get_pixels()))
grayed = IP.grayscale(test)
print(grayed.get_pixels())
