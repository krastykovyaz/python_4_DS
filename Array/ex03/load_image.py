from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display_image(image_array):
    """
    Display the given image array using Matplotlib.

    Args:
        image_array (numpy.ndarray): The image array to display.
    """
    plt.imshow(image_array, cmap='gray')
    plt.colorbar()
    plt.show()


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and display it.

    Args:
        path (str): The path to the image file.

    Returns:
        numpy.ndarray or None:
        The loaded image array if successful,
        None otherwise.
    """
    try:
        # Open the image using Pillow
        image = Image.open(path)
        # Get the format and size of the original image
        image_shape = image.size + (len(image.getbands()),)
        image_shape = image_shape[1], image_shape[0], image_shape[2]
        print(f"The shape of image is: {image_shape}")

        # Convert the image to a numpy array
        image_array = np.array(image)
        print(image_array)

        # Display the original image
        display_image(image_array)

        return image_array
    except Exception as e:
        print(f"Error: {e}")
        return None
