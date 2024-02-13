def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values based on height and weight lists.

    Args:
        height (list): A list of heights.
        weight (list): A list of weights.

    Raises:
        TypeError: If height or weight is not a list.
        ValueError: If height and weight lists have different lengths.
        TypeError: If height or weight elements are not integers or floats.

    Returns:
        list: A list of BMI values.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Both height and weight must be lists")

        if len(height) != len(weight):
            raise ValueError(
                "Height and weight lists must have the same length")

        bmi_values = []
        for h, w in zip(height, weight):
            if not isinstance(
                h, (int, float)
            ) or not isinstance(w, (int, float)):
                raise TypeError(
                    "Height and weight must be integers or floats")
            # Calculate BMI
            bmi = w / (h ** 2)
            bmi_values.append(bmi)

        return bmi_values
    except Exception as e:
        print(e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a BMI limit to the given list of BMI values.

    Args:
        bmi (list): A list of BMI values.
        limit (float): The BMI limit to apply.

    Raises:
        TypeError: If bmi is not a list or contains non-numeric elements.

    Returns:
        list: A list indicating whether each BMI value exceeds the limit.
    """
    try:
        is_any = all(isinstance(x, (int, float)) for x in bmi)
        if not isinstance(bmi, list) or not is_any:
            raise TypeError("BMI must be a list of integers or floats")

        return [b > limit for b in bmi]
    except Exception as e:
        print(e)
