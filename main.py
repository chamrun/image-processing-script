from utils import *
import numpy as np


def gray_scaled_filter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def custom_filter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def scale_img(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def crop_img(img, start_row, end_row, start_column, end_column):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    show_image(image_matrix, title="Input Image")

    gray_scale_pic = gray_scaled_filter(image_matrix)
    show_image(gray_scale_pic, title="Gray Scaled")

    custom_filter(image_matrix)

    cropped_image = crop_img(image_matrix, 50, 300, 50, 225)
    show_image(cropped_image, title="Cropped Image")

    scaled_image = scale_img(image_matrix, 2, 3)
    show_image(scaled_image, title="Scaled Image")
