from load_image import ft_load, display_image


def zoom_image(image_array, start_x, end_x, start_y, end_y):
    """
    Zooms in on a specified region of an image and displays the zoomed portion.

    Args:
        image_array (numpy.ndarray): The array representing the image.
        start_x (int): The starting x-coordinate of the region to zoom in.
        end_x (int): The ending x-coordinate of the region to zoom in.
        start_y (int): The starting y-coordinate of the region to zoom in.
        end_y (int): The ending y-coordinate of the region to zoom in.

    Returns:
        None
    """
    try:
        # Zoom in on the specified region
        zoomed_image = image_array[start_y:end_y, start_x:end_x, 0:1]

        # Get the format and size of the zoomed image
        zoomed_shape = zoomed_image.shape

        # Display the zoomed image
        print(f"New shape after slicing: {zoomed_shape} or {zoomed_shape[:2]}")
        display_image(zoomed_image)
        print(zoomed_image)

    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Main function to load an image, zoom in on a
    specified region, and display the zoomed portion.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        zoom_image(img, 300, 700, 200, 600)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
