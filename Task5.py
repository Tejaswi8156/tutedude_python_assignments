# Task 5: Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
num = int(input("Enter a Number : "))

# Calling the function and displaying the result
fact = factorial(num)
print(f"Factorial of {num} is : {fact}")
