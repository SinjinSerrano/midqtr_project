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
    print("========================== Testing negate(image)")
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

    #  Test grayscale(image)
    print("========================== Testing grayscale(image)")
    print("Using previous RGB Instances:")
    print("Making grayscale Instances")
    test_img0_gray = ImageProcessing.grayscale(test_img0)
    test_img1_gray = ImageProcessing.grayscale(test_img1)
    test_img2_gray = ImageProcessing.grayscale(test_img2)
    print("Exporting grayscale images")
    runner.img_save('img/out/dsc20_grayscale.png', test_img0_gray)
    runner.img_save('img/out/blue_gradient_grayscale.png', test_img1_gray)
    runner.img_save('img/out/pepe_grayscale.png', test_img2_gray)

    #  Test clear_channel(image)
    print("========================== Testing clear_channel(image, channel)")
    print("Original Pixels: " + str(img.get_pixels()))
    print("Cleared Pixels (red):  " + str(ImageProcessing.clear_channel(img, 0).get_pixels()))
    print("Using previous RGB Instances:")
    print("Making cleared Instances")
    test_img0_clear_red = ImageProcessing.clear_channel(test_img0, 0)
    test_img0_clear_green = ImageProcessing.clear_channel(test_img0, 1)
    test_img0_clear_blue = ImageProcessing.clear_channel(test_img0, 2)
    test_img1_clear_red = ImageProcessing.clear_channel(test_img1, 0)
    test_img1_clear_green = ImageProcessing.clear_channel(test_img1, 1)
    test_img1_clear_blue = ImageProcessing.clear_channel(test_img1, 2)
    test_img2_clear_red = ImageProcessing.clear_channel(test_img2, 0)
    test_img2_clear_green = ImageProcessing.clear_channel(test_img2, 1)
    test_img2_clear_blue = ImageProcessing.clear_channel(test_img2, 2)
    print("Exporting cleared channel images")
    runner.img_save('img/out/dsc20_clear_red.png', test_img0_clear_red)
    runner.img_save('img/out/dsc20_clear_green.png', test_img0_clear_green)
    runner.img_save('img/out/dsc20_clear_blue.png', test_img0_clear_blue)
    runner.img_save('img/out/blue_gradient_clear_red.png', test_img1_clear_red)
    runner.img_save('img/out/blue_gradient_clear_green.png', test_img1_clear_green)
    runner.img_save('img/out/blue_gradient_clear_blue.png', test_img1_clear_blue)
    runner.img_save('img/out/pepe_clear_red.png', test_img2_clear_red)
    runner.img_save('img/out/pepe_clear_green.png', test_img2_clear_green)
    runner.img_save('img/out/pepe_clear_blue.png', test_img2_clear_blue)

    #  Test crop(image)
    print("========================== Testing crop(image, tl_row, tl_col, target_size)")
    print("Original Pixels: " + str(img.get_pixels()))
    print("Cropped Pixels:  " + str(ImageProcessing.crop(img, 1, 1, (2,2)).get_pixels()))
    print("Using previous RGB Instances:")
    print("Making cropped Instances")
    test_img0_crop0 = ImageProcessing.crop(test_img0, 50, 75, (75, 50))
    test_img0_crop1 = ImageProcessing.crop(test_img0, 100, 50, (100, 150))
    test_img0_crop2 = ImageProcessing.crop(test_img0, 25, 25, (999, 999))
    test_img1_crop0 = ImageProcessing.crop(test_img1, 0, 10, (10, 100))
    test_img2_crop0 = ImageProcessing.crop(test_img2, 3, 3, (3, 3))
    print("Exporting cropped images")
    runner.img_save('img/out/dsc20_cropped_0.png', test_img0_crop0)
    runner.img_save('img/out/dsc20_cropped_1.png', test_img0_crop1)
    runner.img_save('img/out/dsc20_cropped_2.png', test_img0_crop2)
    runner.img_save('img/out/blue_gradient_cropped_0.png', test_img1_crop0)
    runner.img_save('img/out/pepe_cropped_0.png', test_img2_crop0)

    #  Test chroma_key(chroma_image, background_image, color)
    print("========================== Testing crop(chroma_image, background_image, color)")
    print("Using previous RGB Instances:")
    print("Using DSC20 as chroma key and blue_gradient as background.")
    test_img0_chroma0 = ImageProcessing.chroma_key(test_img0, test_img1, (255,255,255))
    test_img0_chroma1 = ImageProcessing.chroma_key(test_img0, test_img1, (255,205,210))
    print("Exporting chroma-keyed images")
    runner.img_save('img/out/dsc20_chroma_0.png', test_img0_chroma0)
    runner.img_save('img/out/dsc20_chroma_1.png', test_img0_chroma1)

    #  Test rotate_180(image)
    print("========================== Testing crop(chroma_image, background_image, color)")
    print("Using previous RGB Instances:")
    test_img0_rotated = ImageProcessing.rotate_180(test_img0)
    test_img1_rotated = ImageProcessing.rotate_180(test_img1)
    test_img2_rotated = ImageProcessing.rotate_180(test_img2)
    print("Exporting rotated images")
    runner.img_save('img/out/dsc20_rotated.png', test_img0_rotated)
    runner.img_save('img/out/blue_gradient_rotated.png', test_img1_rotated)
    runner.img_save('img/out/pepe_rotated.png', test_img2_rotated)

main()