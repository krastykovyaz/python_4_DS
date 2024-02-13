from PIL import Image
import numpy as np
from pimp_image import plot_image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path.

    Parameters:
    - path (str): The path to the image file.

    Returns:
    - np.ndarray: The image data as a NumPy array.

    This function loads an image from
    the specified path using PIL (Python Imaging Library)
    and converts it into a NumPy array.
    It also plots the original image.
    """
    try:
        # Open the image using PIL
        image = Image.open(path)
        # Convert the image to a NumPy array
        array = np.array(image)
        # Plot the original image
        plot_image("Original Image", array)
        return array
    except Exception as e:
        print(f"Error loading image: {e}")
        raise
