
    
def safe_divide(numerator, denominator):
    try:
        float_numerator = float(numerator)
        float_denominator = float(denominator)
        
        if float_denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        
        result = float_numerator / float_denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."























