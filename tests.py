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

#Testing the vote code
choices = ['h','e','h','e','e','r','h']
count = {}
for choice in choices:
    if not choice in count:
        count[choice] = 1
    else:
        count[choice] += 1
print(count)
highest = 0
option = None
for choice, amount in count.items():
    if highest < amount:
        option = choice
        highest = amount
    elif highest == amount:
        option = np.random.choice([option, choice])
print(option)

#Testing the sort on tuples
tuples = [(6, '4'), (3.1, '1'), (5.3, '3'), (4, '2')]
tuples.sort()
close = [tuple[1] for tuple in tuples]
print(close)
