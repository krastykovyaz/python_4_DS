from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image file from the specified path and return it as a NumPy array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image data as a NumPy array.

    Raises:
        Exception: If there is an error loading the image.
    """
    try:
        # Open the image file
        image = Image.open(path)

        # Get format and shape information
        image_shape = (image.height, image.width, 3)

        print(f"The shape of the image is: {image_shape}")

        # Convert the image to a NumPy array
        image_array = np.array(image)

        return image_array

    except Exception as e:
        raise Exception(f"Error loading image: {e}")
