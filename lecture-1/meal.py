'''
In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
'''


def main():
    user_input = input('What time is it? ')
    print(convert(user_input)) if convert(user_input) else None

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if 7 <= hours < 8 or (hours == 8 and minutes == 0):
        return "breakfast time"
    elif 12 <= hours < 13 or (hours == 13 and minutes == 0):
        return "lunch time"
    elif 18 <= hours < 19 or (hours == 19 and minutes == 0):
        return "dinner time"
    else:
        return  # Not time for a meal, do not output anything

if __name__ == "__main__":
    main()