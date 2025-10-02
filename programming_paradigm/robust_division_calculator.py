def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats, handling non-numeric values
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    

    try:
        # Perform division, handling division by zero
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    

        