import numpy as np
import matplotlib.pyplot as plt

def plot_image(title, image):
    """
    Plot the given image with the specified title.

    Args:
        title (str): The title of the plot.
        image (ndarray): The image array to plot.
    """
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)  # Specify cmap and the range of values
    plt.title(title)
    plt.axis('off')
    plt.show()

def ft_invert(array):
    """
    Inverts the color of the image received.

    Args:
        array (ndarray): The image array to invert.
    """
    array_ = array.copy()
    # Plot the inverted image
    plot_image("Inverted Image", 255 - array_)

def ft_red(array):
    """
    Filters the image to keep only the red channel.

    Args:
        array (ndarray): The image array.
    """
    array_ = array.copy()
    result = np.zeros_like(array_)
    result[:, :, 0] = array_[:, :, 0]
    # Plot the red channel
    plot_image("Red Channel", result)

def ft_green(array):
    """
    Filters the image to keep only the green channel.

    Args:
        array (ndarray): The image array.
    """
    array_ = array.copy()
    result = np.zeros_like(array_)
    result[:, :, 1] = array_[:, :, 1]
    # Plot the green channel
    plot_image("Green Channel", result)

def ft_blue(array):
    """
    Filters the image to keep only the blue channel.

    Args:
        array (ndarray): The image array.
    """
    array_ = array.copy()
    result = np.zeros_like(array_)
    result[:, :, 2] = array_[:, :, 2]
    # Plot the blue channel
    plot_image("Blue Channel", result)

def ft_grey(array):
    """
    Converts the image to grayscale.

    Args:
        array (ndarray): The image array.
    """
    array_ = array.copy()
    result = np.dot(array_[..., :3], [0.2989, 0.587, 0.114])
    # Plot the grey image
    plot_image("Grey Image", result)

def main():
    # Load the image (replace this with your image loading code)
    image = np.random.randint(0, 256, size=(100, 100, 3)).astype(np.uint8)

    # Example usage
    ft_invert(image)
    ft_red(image)
    ft_green(image)
    ft_blue(image)
    ft_grey(image)

if __name__ == "__main__":
    main()
