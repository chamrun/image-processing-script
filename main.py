from utils import *
import numpy as np

def grayScaledFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass

def customFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def scaleImg(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def cropImg(img, start_row, end_row, start_column, end_column):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    grayScalePic = grayScaledFilter(image_matrix)
    showImage(grayScalePic, title="Gray Scaled")

    customFilter(image_matrix)

    croppedImage = cropImg(image_matrix, 50, 300, 50, 225)
    showImage(croppedImage, title="Cropped Image")

    scaledImage = scaleImg(image_matrix, 2, 3)
    showImage(scaledImage, title="Scaled Image")
