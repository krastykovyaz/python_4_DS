from load_image import ft_load
from rotate import rotate_image

def main():
    """
    Main function to test the rotation of an image.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        rotate_image(img, 300, 700, 200, 600)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()