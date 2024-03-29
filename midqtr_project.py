"""
DSC 20 Mid-Quarter Project
Name: Sinjin Serrano and David Perez
PID:  A16687329 / A16686629
"""

# Part 1: RGB Image #
class RGBImage:
    """
    Creates a RGBImage class, an abstraction of an image using RGB colorspace.

    The RGB color model is a tuple of three integers (intensity) indicating
    the presence of color in a given pixel (Red, Green, Blue).
    Values are unsigned 8-bit integers, meaning they range from 0,
    indicating no presence, and 255, indicating full presence.

    'pixels' is a three-dimensional list used to store RGBImage's data.
    The first dimension is an integer indicating which color channel is
    represented (0 - red, 1 - green, 2 - blue)
    The second dimension indicates the pixel's row index, while the third
    dimension indicates the pixel's column index.
    The value stored there is a three-element tuple representing using the
    RGB color model to store that pixel's value.
    """

    def __init__(self, pixels):
        """
        A constructor for RGBImage that defines the image's pixel list.
        Assume:
            - Index of channel c is guaranteed to be 0, 1, or 2
            - Each channel contains a valid (row x col) matrix
        """
        self.pixels = pixels

    def size(self):
        """
        A getter method that calculates the size of the image and returns
        a tuple containing (rows, columns).
        """
        rows = len(self.pixels[0])
        cols = len(self.pixels[0][0])
        return (rows, cols)

    def get_pixels(self):
        """
        A getter method that returns a deep copy of the pixels matrix.
        """
        return [[[intensity for intensity in row] for row in channel]\
             for channel in self.pixels]

    def copy(self):
        """
        A method which returns a copy of this instance, using a deep copy of
        the pixels matrix.
        """
        return RGBImage(self.get_pixels())

    def get_pixel(self, row, col):
        """
        A getter method which returns a three-element tuple containing the
        color of the pixel at the specified row and col.
        """
        assert isinstance(row, int) and isinstance(col, int)
        assert 0 <= row < self.size()[0] and 0 <= col < self.size()[1]
        iRED = 0
        iGREEN = 1
        iBLUE = 2
        return (self.pixels[iRED][row][col], self.pixels[iGREEN][row][col],\
        self.pixels[iBLUE][row][col])

    def set_pixel(self, row, col, new_color):
        """
        A setter method which updates the pixel at the specified row and col
        with a new color, represented by a three-element tuple.
        If an intensity is represented by -1, do not update the intensity
        at that channel.
        """
        assert isinstance(row, int) and isinstance(col, int)
        assert 0 <= row < self.size()[0] and 0 <= col < self.size()[1]
        assert all([isinstance(i, int) for i in new_color])
        assert all([-1 <= i <= 255 for i in new_color])
        iRED = 0
        iGREEN = 1
        iBLUE = 2
        color = self.get_pixel(row, col)
        red = color[iRED] if new_color[iRED] == -1\
            else new_color[iRED]
        green = color[iGREEN] if new_color[iGREEN] == -1\
            else new_color[iGREEN]
        blue = color[iBLUE] if new_color[iBLUE] == -1\
            else new_color[iBLUE]
        self.pixels[iRED][row][col] = red
        self.pixels[iGREEN][row][col] = green
        self.pixels[iBLUE][row][col] = blue


# Part 2: Image Processing Methods #
class ImageProcessing:
    """
    A class that contains several different static methods used to manipulate
    RGBImage objects. New instances are returned after being passed through
    these methods.
    """

    @staticmethod
    def negate(image):
        """
        This code takes an image and creates a version that inverts/negates
        the color values of each pixel by doing the subtraction, 255 - current
        color value.
        """

        negated_pixels = [[[255 - image.get_pixel(row_ind, col_ind)[run] \
        for col_ind in range(image.size()[1])]\
        for row_ind in range(image.size()[0])]\
        for run in range(3)]

        return RGBImage(negated_pixels)

    @staticmethod
    def grayscale(image):
        """
        This code takes an image and creates a version that is a grayscale
        version of the original by taking adding the color values at a pixel,
        averaging them and setting all three values to the new value.
        """

        gray_pixels = [[[((image.get_pixel(row_ind, col_ind)[0] +\
        image.get_pixel(row_ind, col_ind)[1] + \
        image.get_pixel(row_ind, col_ind)[2]) // 3) \
        for col_ind in range(image.size()[1])]\
        for row_ind in range(image.size()[0])]\
        for run in range(3)]


        return RGBImage(gray_pixels)

    @staticmethod
    def clear_channel(image, channel):
        """
        A method which takes an RGBImage and returns a version with the
        specified channel cleared (their intensities set to 0).
        """
        iRED = 0
        iGREEN = 1
        iBLUE = 2
        pixels = image.get_pixels()
        red = pixels[iRED]
        if channel == iRED:
            red = [[0 for _ in row] for row in pixels[iRED]]
        green = pixels[iGREEN]
        if channel == iGREEN:
            green = [[0 for _ in row] for row in pixels[iGREEN]]
        blue = pixels[iBLUE]
        if channel == iBLUE:
            blue = [[0 for _ in row] for row in pixels[iBLUE]]
        return RGBImage([red, green, blue])

    @staticmethod
    def crop(image, tl_row, tl_col, target_size):
        """
        A method which takes an RGBImage and returns a version cropped,
        the top-left denoted by tl_row and tl_col, and the size denoted
        by target_size where possible.
        """
        orig_size = image.size()
        cropped_rows = target_size[0] if \
            orig_size[0] - tl_row - target_size[0] > 0 else \
                orig_size[0] - tl_row
        cropped_cols = target_size[1] if \
            orig_size[1] - tl_col - target_size[1] > 0 else \
                orig_size[1] - tl_col
        new_pixels = [[[intensity for c, intensity in enumerate(row) \
            if tl_col <= c < tl_col + cropped_cols] \
            for r, row in enumerate(channel) \
            if tl_row <= r < tl_row + cropped_rows] \
            for channel in image.get_pixels()]
        return RGBImage(new_pixels)

    @staticmethod
    def chroma_key(chroma_image, background_image, color):
        """
        A choroma key algorithm that returns a copy of an RGBImage, where
        pixels that match the specified color are replaced by the
        corresponding pixel in the background image.
        """
        img_size = chroma_image.size()
        assert isinstance(chroma_image, RGBImage) \
            and isinstance(background_image, RGBImage)
        assert img_size == background_image.size()
        rows = img_size[0]
        cols = img_size[1]
        new_img = RGBImage(chroma_image.get_pixels())
        for r in range(rows):
            for c in range(cols):
                if color == chroma_image.get_pixel(r, c):
                    bg_color = background_image.get_pixel(r, c)
                    new_img.set_pixel(r, c, bg_color)
        return new_img


    # rotate_180 IS FOR EXTRA CREDIT (points undetermined)
    @staticmethod
    def rotate_180(image):
        """
        A method which returns a 180 degree rotation of an image.
        """
        pixels = image.get_pixels()
        new_pixels = [[[intensity for intensity in row[::-1]] \
            for row in channel[::-1]] for channel in pixels]
        return RGBImage(new_pixels)


# Part 3: Image KNN Classifier #
class ImageKNNClassifier:
    """
    This class uses a data set to predict the tag for a given image sent in.
    It does this by finding the distance between every pixel and every channel
    in those pixels. By comparing the most common tags, it decides the best
    fit for the image using the methods below.
    """
    data = []

    def __init__(self, n_neighbors):
        """
        This code initilizes a ImageKNNClassifier class that has k_neighbors
        as an input parameter and data in the form of a tuple with an image
        and a image tag string.
        """
        self.n_neighbors = n_neighbors
        ImageKNNClassifier.data = []

    def fit(self, data):
        """
        This code fits a data set that is greater than the number of
        neighbors, if it has not already been assigned data.
        """
        assert len(data) > self.n_neighbors
        assert len(ImageKNNClassifier.data) == 0
        ImageKNNClassifier.data = data

    @staticmethod
    def distance(image1, image2):
        """
        This code compares every pixel intensity in every channel
        for two images and performs a Euclid distance calculation between
        them.
        """
        assert isinstance(image1, RGBImage) and isinstance(image2, RGBImage)
        assert image1.size() == image2.size()
        distance = (sum([(image1.get_pixel(row_ind, col_ind)[channel]\
        - image2.get_pixel(row_ind, col_ind)[channel])**2 \
        for col_ind in range(image1.size()[1])\
        for row_ind in range(image1.size()[0])\
        for channel in range(3)]))**1/2
        return distance

    @staticmethod
    def vote(candidates):
        """
        This code takes a list of tags equal to the amount of neighbors
        in k_neighbors. It first creates a dictionary of tags and the
        count of how many times they show up. It then sorts them and
        returns the tag with the highest frequency. If two tags are the
        highest, it randomly chooses between them.
        """
        label_counter = {}
        for candidate in candidates:
            if not candidate in label_counter:
                label_counter[candidate] = 1
            else:
                label_counter[candidate] += 1
        highest = 0
        option = None
        for label, amount in label_counter.items():
            if highest < amount:
                option = label
                highest = amount
        return option


    def predict(self, image):
        """
        This code first checks if the dataset in the class is filled. If it
        is, it then sorts a list of tuple objects with distances and tags,
        and finally finds the n_neighbors that are the closest and compares
        tags using vote().
        """
        assert len(ImageKNNClassifier.data) > 0
        distance_tag = [(ImageKNNClassifier.distance(image, tag_img[0]),\
        tag_img[1]) for tag_img in ImageKNNClassifier.data]
        distance_tag.sort()
        close_tag = [tag[1] for tag in distance_tag]
        return ImageKNNClassifier.vote(close_tag[0:self.n_neighbors - 1])
