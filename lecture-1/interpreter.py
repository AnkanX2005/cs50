'''
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
'''


def main():
    user_input = input("Expression: ")
    user_input = user_input.split(' ')

    print(interpreter(user_input))

def interpreter(expression):
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    if y == '+':
        return f"{x + z:.1f}"
    elif y == '-':
        return f"{x - z:.1f}"
    elif y == '*':
        return f"{x * z:.1f}"
    elif y == '/':
        return f"{x / z:.1f}"
    else:
        return 'Invalid Expression !!!!!!'


main()