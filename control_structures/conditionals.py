number = 10
if number > 0:
    print("The number is positive.")
else:
    print("The number is not-positive.")

number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"The number {number} is {result}.")

num1 = 10
num2 = 5
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
