import math

def safe_divide(numerator, denominator):
   
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Invalid input. Please enter numeric values."

    if math.isnan(num) or math.isnan(den):
        return "Error: Invalid input. Please enter numeric values."

    if math.isinf(num) and math.isinf(den):
        return "Error: Invalid input. Please enter numeric values."

    if den == 0.0:
        return "Error: Division by zero is not allowed."

    result = num / den

    if math.isnan(result):
        return "Error: Invalid input. Please enter numeric values."

    return result
