"""
doctests.py
"""
from midqtr_project import RGBImage
from midqtr_project import ImageProcessing
import midqtr_project_runner as runner

# Not the most professional tests but it gets the job done.

def main():
    my_pixels = [
        [
            # channel 0: red (2 rows x 3 columns)
            [206, 138, 253],
            [204, 208, 220]

        ],
        [
            # channel 1: green (2 rows x 3 columns)
            [214, 190, 173],
            [209, 136, 131]
        ],
        [
            # channel 2: blue (2 rows x 3 columns)
            [233, 188, 214],
            [163, 169, 131]
        ],
    ]
    img = RGBImage(my_pixels)
    #  Test size(self)
    print("========================== Testing size(self)")
    my_size = img.size()
    print("Expected: (2, 3)")
    print("Got:      " + str(my_size))

    #  Test get_pixels(self)
    print("========================== Testing get_pixels(self)")
    new_pixels = img.get_pixels()    
    print("deepcopy: " + str(new_pixels))
    print("original_id: " + str(id(img)))
    print("deepcopy_id: " + str(id(new_pixels)))

    #  Test copy(self)
    print("========================== Testing copy(self)")
    new_img = img.copy()
    print("original: " + str(img))
    print("copy    : " + str(new_img))

    #  Test get_pixel(self, row, col)
    print("========================== Testing get_pixel(self, row, col)")
    my_pixel = img.get_pixel(1, 1)
    print("Expected: (208, 136, 169)")
    print("Got:      " + str(my_pixel))


    #  Test set_pixel(self, row, col, new_color)
    print("========================== Testing set_pixel(self, row, col, new_color)")
    print("Setting row 1, col 2 to (128, 128, 128)")
    img.set_pixel(1, 2, (128, 128, 128))
    print(str(img.get_pixels()))

    print("Setting row 1, col 2 to (-1, 8, 0)")
    img.set_pixel(1, 2, (-1, 8, 0))
    print(str(img.get_pixels()))

    print("Setting row 0, col 0 to (-1, -1, -1)")
    img.set_pixel(0, 0, (-1, -1, -1))
    print(str(img.get_pixels()))
    print("--------- Testing Asserts")

    #  Test negate(image)
    print("========================== Testing set_pixel(self, row, col, new_color)")
    print("Making RGB Instances")
    test_img0 = runner.img_read('img/dsc20.png')
    test_img1 = runner.img_read('img/blue_gradient.png')
    test_img2 = runner.img_read('img/pepe.png')
    print("Making Inverted Instances")
    test_img0_inverted = ImageProcessing.negate(test_img0)
    test_img1_inverted = ImageProcessing.negate(test_img1)
    test_img2_inverted = ImageProcessing.negate(test_img2)
    print("Exporting inverted images")
    runner.img_save('img/out/dsc20_inverted.png', test_img0_inverted)
    runner.img_save('img/out/blue_gradient_inverted.png', test_img1_inverted)
    runner.img_save('img/out/pepe_inverted.png', test_img2_inverted)


main()