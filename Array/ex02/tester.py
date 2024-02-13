from load_image import ft_load

def main():
    """
    Main function to test loading an image.
    """
    try:
        image_path = "landscape.jpg"
        image_data = ft_load(image_path)
        print(image_data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()