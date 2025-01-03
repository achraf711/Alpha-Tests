def gcd(a, b):
    try:
        # Ensure the inputs are integers
        a = int(a)
        b = int(b)
        
        # Compute the GCD using the Euclidean algorithm
        while b != 0:
            a, b = b, a % b
        return a
    
    except ValueError:
        return "Error: Please enter valid integers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = gcd(num1, num2)
    
    if isinstance(result, int):
        print(f"The greatest common divisor of {num1} and {num2} is {result}.")
    else:
        print(result)
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
