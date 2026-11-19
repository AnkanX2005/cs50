'''
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
'''

def main():
    user_input = input('Item: ')
    grocery_list = {}
    while True:
        try:
            grocery_list[user_input] = grocery_list.get(user_input, 0) + 1
            user_input = input('Item: ')
            if user_input == 'control-d':
                break
        except EOFError:
            pass

    # Sort items alphabetically and display with counts
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")


if __name__ == "__main__":
    main()