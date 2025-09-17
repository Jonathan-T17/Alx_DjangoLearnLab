# simple calculator using match-case statement

# prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")


# perform the  calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result is: {result}")
    case "/":
        if num2 == 0:
            result = "cannot divide by zero"
            print(result)
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    case _:
        print("Invalid operation! Please choose +, -, *, or /.")
