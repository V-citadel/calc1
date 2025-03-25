user_name = input("Hello! What's your name? ")
print(f"Nice to meet you, {user_name}!")


first_number = float(input("Please enter the 1st number: "))
second_number = float(input("Please enter the 2nd number: "))
operation = input("Please enter an operation (+, -, *, /): ")


if operation == "+":
    result = first_number + second_number
    print(f"{user_name}, the result of {first_number} + {second_number} is {result}.")
elif operation == "-":
    result = first_number - second_number
    print(f"{user_name}, the result of {first_number} - {second_number} is {result}.")
elif operation == "*":
    result = first_number * second_number
    print(f"{user_name}, the result of {first_number} * {second_number} is {result}.")
elif operation == "/":
    if second_number != 0:  
        result = first_number / second_number
        print(f"{user_name}, the result of {first_number} / {second_number} is {result}.")
    else:
        print(f"Sorry, {user_name}. Division by zero is not allowed.")
else:
    print(f"Invalid operation, {user_name}! Please choose +, -, *, or /.")