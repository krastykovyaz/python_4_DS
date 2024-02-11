def all_thing_is_obj(obj: any) -> int:
    """
    Print the type of the object.

    Args:
        obj (any): The object to determine the type of.

    Returns:
        int: The length of the object if it's a list, tuple, set, or dictionary. Otherwise, returns 42.
    """
    # Print the object type
    if isinstance(obj, list):
        print(f"List : <class '{type(obj).__name__}'>")
        return len(obj)
    elif isinstance(obj, tuple):
        print(f"Tuple : <class '{type(obj).__name__}'>")
        return len(obj)
    elif isinstance(obj, set):
        print(f"Set : <class '{type(obj).__name__}'>")
        return len(obj)
    elif isinstance(obj, dict):
        print(f"Dict : <class '{type(obj).__name__}'>")
        return len(obj)
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen : <class '{type(obj).__name__}'>")
    else:
        return 42

def main():
    """
    Main function to test the all_thing_is_obj function.
    """
    # Test different types of objects
    obj_list = [1, 2, 3]
    obj_tuple = (1, 2, 3)
    obj_set = {1, 2, 3}
    obj_dict = {'a': 1, 'b': 2, 'c': 3}
    obj_str = "apple"

    print(all_thing_is_obj(obj_list))
    print(all_thing_is_obj(obj_tuple))
    print(all_thing_is_obj(obj_set))
    print(all_thing_is_obj(obj_dict))
    print(all_thing_is_obj(obj_str))
    print(all_thing_is_obj(42))

if __name__ == "__main__":
    main()
