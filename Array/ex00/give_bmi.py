def give_bmi(height, weight):
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists")
    
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")

    bmi_values = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight must be integers or floats")
        
        # Calculate BMI
        bmi = w / (h ** 2)
        bmi_values.append(bmi)

    return bmi_values

def apply_limit(bmi, limit):
    if not isinstance(bmi, list) or not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("BMI must be a list of integers or floats")

    return [b > limit for b in bmi]

if __name__=='__main__':
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
