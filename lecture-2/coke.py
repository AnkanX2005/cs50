'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''


def main():
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        print(f'Amount due: {amount_due - total_inserted} cents')
        coin = int(input("Insert coin ( 5, 10, 25 ): "))
        if coin in [5, 10, 25]:
            total_inserted += coin
        else:
            print("Invalid coin. Please insert a valid coin ")

    change = total_inserted - amount_due
    print(f'Change owed: {change} cents')

if __name__ == "__main__":
    main()