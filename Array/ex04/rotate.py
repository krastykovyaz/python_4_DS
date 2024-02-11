from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import loading_img

def display_image(image_array):
    """
    Display the given image array.

    Args:
        image_array (numpy.ndarray): The image array to display.
    """
    plt.imshow(image_array, cmap='gray')
    plt.colorbar()
    plt.show()

def rotate_image(image_array, start_x, end_x, start_y, end_y):
    """
    Rotate a square part of the image and display it.

    Args:
        image_array (numpy.ndarray): The input image array.
        start_x (int): The starting x-coordinate of the square part.
        end_x (int): The ending x-coordinate of the square part.
        start_y (int): The starting y-coordinate of the square part.
        end_y (int): The ending y-coordinate of the square part.
    """
    try:
        square_part = np.array(image_array)[start_y:end_y, start_x:end_x, 0:1]
        square_shape = square_part.shape
        print(f"The shape of the image is: {square_shape} or {square_shape[:2]}")
        display_image(square_part)

        image_array = image_array.convert('L')
        square_part = np.array(image_array)[start_y:end_y, start_x:end_x]
        transposed_square = np.transpose(square_part)

        transposed_shape = transposed_square.shape
        print(f"New shape after Transpose: {transposed_shape}")
        display_image(transposed_square)

    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Main function to test the rotation of an image.
    """
    try:
        path = "animal.jpeg"
        img = loading_img(path)
        rotate_image(img, 300, 700, 200, 600)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
