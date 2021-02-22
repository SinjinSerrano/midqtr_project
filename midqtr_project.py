"""
DSC 20 Mid-Quarter Project
Name: TODO
PID:  TODO
"""

# Part 1: RGB Image #
class RGBImage:
    """
    TODO: add description
    """

    def __init__(self, pixels):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #
        self.pixels = ...  # initialze the pixels list here

    def size(self):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def get_pixels(self):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def copy(self):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def get_pixel(self, row, col):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def set_pixel(self, row, col, new_color):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #


# Part 2: Image Processing Methods #
class ImageProcessing:
    """
    TODO: add description
    """

    @staticmethod
    def negate(image):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

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
