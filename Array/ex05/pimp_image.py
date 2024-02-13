import numpy as np
import matplotlib.pyplot as plt


def plot_image(title: str, image: np.ndarray) -> np.ndarray:
    """
    Plot the given image with the specified title.

    Args:
        title (str): The title of the plot.
        image (ndarray): The image array to plot.
    """
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    try:
        array_ = array.copy()
        result = 255 - array_
        # Plot the inverted image
        print(f"The shape of the image is: {result.shape}")
        print(result)
        plot_image("Inverted Image", result)
        return result
    except Exception as e:
        print(e)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Filters the image to keep only the red channel.

    Args:
        array (ndarray): The image array.
    """
    try:
        array_ = array.copy()
        result = np.zeros_like(array_)
        result[:, :, 0] = array_[:, :, 0]
        # Plot the red channel
        print(f"The shape of the image is: {result.shape}")
        print(result)
        plot_image("Red Channel", result)
        return result
    except Exception as e:
        print(e)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Filters the image to keep only the green channel.

    Args:
        array (ndarray): The image array.
    """
    try:
        array_ = array.copy()
        result = np.zeros_like(array_)
        result[:, :, 1] = array_[:, :, 1]
        # Plot the green channel
        print(f"The shape of the image is: {result.shape}")
        print(result)
        plot_image("Green Channel", result)
        return result
    except Exception as e:
        print(e)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Filters the image to keep only the blue channel.

    Args:
        array (ndarray): The image array.
    """
    try:
        array_ = array.copy()
        result = np.zeros_like(array_)
        result[:, :, 2] = array_[:, :, 2]
        # Plot the blue channel
        print(f"The shape of the image is: {result.shape}")
        print(result)
        plot_image("Blue Channel", result)
        return result
    except Exception as e:
        print(e)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.

    Args:
        array (ndarray): The image array.
    """
    try:
        array_ = array.copy()
        result = np.dot(array_[..., :3], [0.2989, 0.587, 0.114])
        # Plot the grey image
        print(f"The shape of the image is: {result.shape}")
        print(result)
        plot_image("Grey Image", result)
        return result
    except Exception as e:
        print(e)
