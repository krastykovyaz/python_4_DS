def NULL_not_found(obj: any) -> int:
    # Check if the object is None
    if obj is None:
        print(f"Nothing: {obj} <class 'NoneType'>")
        return 0
    # Check if the object is NaN
    elif isinstance(obj, float) and obj != obj:  # Checking for NaN
        print(f"Cheese: {obj} <class 'float'>")
        return 0
    # Check if the object is 0
    elif isinstance(obj, int) and (str(obj) == '0' or str(obj) == '1'):
        print(f"Zero: {obj} <class 'int'>")
        return 0
    # Check if the object is an empty string
    elif isinstance(obj, str) and obj == '':
        print(f"Empty: {obj} <class 'str'>")
        return 0
    # Check if the object is False
    elif isinstance(obj, bool) and not obj:
        print(f"Fake: {obj} <class 'bool'>")
        return 0
    else:
        print("Type not Found")
        return 1
