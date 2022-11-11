"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


while True:
    user_input = input("> ")
    tokens = user_input.split(' ')
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    if tokens[0] == "q":
        print("Exit")
        break
    
    elif tokens[0] == "+":
        print(add(num1, num2))
        
    elif tokens[0] == "-":
        print(subtract(num1, num2))

    elif tokens[0] == "*":
        print(multiply(num1, num2))

    elif tokens[0] == "/":
        print(divide(num1, num2))
    
# square(x)
    elif tokens[0] == "square":
        print(square(num1))

# cube(x)
    elif tokens[0] == "cube":
        print(cube(num1))

# power(x, y)
    elif tokens[0] == "pow":
        print(power(num1, num2))

# mod(x, y)
    elif tokens[0] == "mod":
        print(mod(num1, num2))


# Replace this with your code

# if the first token is 'pow':
#     call the power function with the other two tokens

# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens
#             (...etc.)