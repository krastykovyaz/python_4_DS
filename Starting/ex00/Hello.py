def modify_data_objects():
    """
    Modify the strings in each data object.
    """
    ft_list = ["Hello", "World!"]
    ft_tuple = ("Hello", "France!")
    ft_set = {"Hello", "Paris!"}
    ft_dict = {"Hello": "42Paris!"}

    # Modify the strings
    ft_list[1] = "World!"
    ft_tuple = ("Hello", "France!")
    ft_set.remove("Paris!")
    ft_set.add("Paris!")
    ft_dict["Hello"] = "42Paris!"

    # Print the modified data objects
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

def main():
    """
    Main function to execute the code.
    """
    modify_data_objects()
    # Add assertion checks if required

if __name__ == "__main__":
    main()
