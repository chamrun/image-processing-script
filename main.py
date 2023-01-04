from utils import *
import numpy as np


def main():
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    # show_image(image_matrix, title="Input Image")

    # gray_scale_pic = gray_scaled_filter(image_matrix)
    # show_image(gray_scale_pic, title="Gray Scaled")
    # return
    #
    # custom_filter(image_matrix)

    cropped_image = crop_img(image_matrix, 100, 700, 100, 300)
    show_image(cropped_image, title="Cropped Image")
    return

    scaled_image = scale_img(image_matrix, 2, 3)
    show_image(scaled_image, title="Scaled Image")


def gray_scaled_filter(img):
    gray_scaled_pic = np.zeros((img.shape[0], img.shape[1], 3), dtype='int')
    log("Gray scaled filter started")
    log(f'length of image matrix is {len(img)}')
    for i in range(len(img)):
        if i % 100 == 0:
            log(f'row {i} is done')

        for j in img[i]:
            # gray = int(0.1 * j[0] + 0.4 * j[1] + 0.5 * j[2])
            # gray_scaled_pic[i][j] = [gray, gray, gray]

            gray_scaled_pic[i][j] = [int(0.5 * j[0]), int(0.5 * j[1]), int(0.5 * j[2])]

    return gray_scaled_pic


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
    cropped_image = np.zeros((end_row - start_row, end_column - start_column, 3), dtype='int')

    for i in range(start_row, end_row):
        for j in range(start_column, end_column):
            cropped_image[i - start_row][j - start_column] = img[i][j]

    return cropped_image


def log(s):
    import datetime
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), s)


if __name__ == "__main__":
    main()
