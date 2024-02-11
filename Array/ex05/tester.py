from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def main():
    """
    Main function to load and manipulate an image.
    """
    # Load the image
    array = ft_load("landscape.jpg")

    # Apply image transformations
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    # Print documentation for ft_invert function
    print(ft_invert.__doc__)

if __name__ == "__main__":
    main()
