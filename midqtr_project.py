"""
DSC 20 Mid-Quarter Project
Name: Sinjin Serrano and David Perez
PID:  A16687329 / A16686629
"""

# Part 1: RGB Image #
class RGBImage:
    """
    TODO: review description
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

    TODO: Test methods.
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
        return (self.pixels[iRED][row][col], self.pixels[iGREEN][row][col], self.pixels[iBLUE][row][col])

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
        # I am almost certain there is a much better way to do this
        self.pixels[iRED][row][col] = red
        self.pixels[iGREEN][row][col] = green
        self.pixels[iBLUE][row][col] = blue



# Part 2: Image Processing Methods #
class ImageProcessing:
    """

    """

    @staticmethod
    def negate(image):
        """

        """

        pixels = [[[255 - image.get_pixel(row_ind, col_ind)[run] \
        for col_ind in range(image.size()[1])]\
        for row_ind in range(image.size()[0])]\
        for run in range(0, 3, 1)]

        return RGBImage(pixels)

    @staticmethod
    def grayscale(image):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def clear_channel(image, channel):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def crop(image, tl_row, tl_col, target_size):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def chroma_key(chroma_image, background_image, color):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    # rotate_180 IS FOR EXTRA CREDIT (points undetermined)
    @staticmethod
    def rotate_180(image):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #


# Part 3: Image KNN Classifier #
class ImageKNNClassifier:
    """
    TODO: add description
    """

    def __init__(self, n_neighbors):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def fit(self, data):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def distance(image1, image2):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def vote(candidates):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def predict(self, image):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #
