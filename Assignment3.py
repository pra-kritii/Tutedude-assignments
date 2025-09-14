#Task1
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = 5
print(f"The factorial of {number} is: {factorial(number)}")


#Task2
import math

num = float(input("Enter a number: "))
sqrt_value = math.sqrt(num)
log_value = math.log(num)
sine_value = math.sin(num)

print(f"Square root of {num}: {sqrt_value}")
print(f"Natural logarithm of {num}: {log_value}")
print(f"Sine of {num} (radians): {sine_value}")
