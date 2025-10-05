def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: division by zero is not allowed."
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."
