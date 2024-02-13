from load_image import ft_load
from zoom import zoom_image

def main():
    """
    Main function to load an image, zoom in on a specified region, and display the zoomed portion.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        zoom_image(img, 300, 700, 200, 600)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()