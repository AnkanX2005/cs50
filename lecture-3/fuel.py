'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

def main():
    user_input = input("Fraction: ")
    print(fuel_percentage(user_input))


def fuel_percentage(fraction):
    while True:
        try:
            x, y = map(int, fraction.split('/'))
            if y >= x >= 0 and y != 0:
                percentage = round((x / y) * 100)
                if percentage <= 1:
                    return "E"
                elif percentage >= 99:
                    return "F"
                else:
                    return f"{percentage}%"
            else:
                fraction = input("Fraction: ")    
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction in the format X/Y where X is a non-negative integer and Y is a positive integer.")   
              # this line will never be reached because the loop will either return a value or prompt the user again for input.

if __name__ == "__main__":
    main()    