def all_thing_is_obj(obj: any) -> int:
    # Print the object type
    if isinstance(obj, list):
        print(f"List : <class '{type(obj).__name__}'>")
    elif isinstance(obj, tuple):
        print(f"Tuple : <class '{type(obj).__name__}'>")
    elif isinstance(obj, set):
        print(f"Set : <class '{type(obj).__name__}'>")
    elif isinstance(obj, dict):
        print(f"Dict : <class '{type(obj).__name__}'>")
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen : <class '{type(obj).__name__}'>")
    else:
        return "Type not found\n42"





