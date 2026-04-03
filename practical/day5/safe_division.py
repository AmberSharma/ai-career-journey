def safe_division(numerator, denominator):
    try:
        print(numerator / denominator)
    except ZeroDivisionError:
        print("Division by zero not allowed")
    except ValueError:
        print("Invalid Input")
    except TypeError:
        print("Invalid Input")

safe_division(-1,10)