'''
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
'''

month_ = [
        "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

months = {}
for i, month in enumerate(month_):
    months[month.lower()] = i + 1

def main():
    year, month, day = convert()
    print(f"{year}-{month:02}-{day:02}")

def convert():
    while True:
        date_input = input("Date: ")

        try:
            if "/" in date_input:
                month, day, year = map(int, date_input.split("/"))
            else:
                month_str, day_str, year_str = date_input.split()
                month = months[month_str.lower()]
                day = int(day_str.rstrip(','))
                year = int(year_str)

            from datetime import date
            date(year, month, day)  # Validate the date
            return year, month, day    
    
        except (ValueError, KeyError):
            pass

if __name__ == "__main__":
    main()        