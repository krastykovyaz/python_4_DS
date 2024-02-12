def all_thing_is_obj(obj: any) -> int:
    """
    Print the type of the object.

    Args:
        obj (any): The object to determine the type of.

    Returns:
        int: The length of the object if it's \
        a list, tuple, set, or dictionary. Otherwise, returns 42.
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
        print("Type not found")
        return 42
