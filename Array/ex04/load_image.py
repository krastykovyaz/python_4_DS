from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display_image(image_array):
    """
    Display the image using matplotlib.

    Args:
        image_array (numpy.ndarray): The image array to display.
    """
    plt.imshow(image_array, cmap='gray')  # Use a grayscale colormap
    plt.colorbar()
    plt.show()


def ft_load(path: str) -> Image:
    """
    Load an image from the given path using Pillow.

    Args:
        path (str): The path to the image file.

    Returns:
        PIL.Image.Image: The loaded image.
    """
    try:
        # Open the image using Pillow
        image = Image.open(path)

        # Get the format and size of the original image
        image_shape = image.size + (len(image.getbands()),)
        image_shape = image_shape[1], image_shape[0], image_shape[2]
        # print(f"The shape of image is: {image_shape}")

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Display the original image
        display_image(image_array)

        return image
    except Exception as e:
        print(f"Error: {e}")
