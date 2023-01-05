from utils import *
import numpy as np


def main():
    image_matrix = get_input('pic.jpg')

    show_image(image_matrix, title="Input Image")

    gray_scale_pic = gray_scaled_filter(image_matrix)
    show_image(gray_scale_pic, title="Gray Scaled")

    filtered_image, reversed_filtered_image = custom_filter(image_matrix)
    show_image(filtered_image, title="Custom Filter")
    show_image(reversed_filtered_image, title="Reversed Custom Filter")

    cropped_image = crop_img(image_matrix, 50, 300, 50, 225)
    show_image(cropped_image, title="Cropped Image")

    scaled_image = scale_img(image_matrix, 2, 3)
    show_image(scaled_image, title="Scaled Image")


def gray_scaled_filter(img):
    filtered_pic = np.zeros((img.shape[0], img.shape[1], 3), dtype='int')
    log("Custom filter started")
    log(f'length of image matrix is {len(img)}')
    for i in range(len(img)):
        if i % 100 == 0:
            log(f'row {i} is done')

        for j_index in range(len(img[i])):
            j = img[i][j_index]
            gray = int(0.3 * j[0] + 0.59 * j[1] + 0.11 * j[2])

            filtered_pic[i][j_index] = [gray, gray, gray]

    return filtered_pic


def scale_img(img, scale_width, scale_height):
    scaled_image = np.zeros((img.shape[0] * scale_height, img.shape[1] * scale_width, 3), dtype='int')

    for i in range(len(img)):
        for j in range(len(img[i])):
            for h in range(scale_height):
                for w in range(scale_width):
                    scaled_image[i * scale_height + h][j * scale_width + w] = img[i][j]

    return scaled_image


def crop_img(img, start_row, end_row, start_column, end_column):
    cropped_image = np.zeros((end_row - start_row, end_column - start_column, 3), dtype='int')

    for i in range(start_row, end_row):
        for j in range(start_column, end_column):
            cropped_image[i - start_row][j - start_column] = img[i][j]

    return cropped_image


def custom_filter(img):
    filter_matrix = np.array([[1, 1, 1], [2, 1, -2], [1, 1, -1]])
    reversed_filter_matrix = np.linalg.inv(filter_matrix)

    filtered_pic = apply_filter(img, filter_matrix)
    reversed_filtered_pic = apply_filter(filtered_pic, reversed_filter_matrix)

    return filtered_pic, reversed_filtered_pic


def log(s):
    import datetime
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), s)


if __name__ == "__main__":
    main()
