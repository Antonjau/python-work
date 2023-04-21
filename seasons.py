import sys
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def main():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")
        sys.exit()
    age_in_minutes = calculate_age_in_minutes(dob)
    print(f"You are {convert_to_words(age_in_minutes)} old in minutes.")


def calculate_age_in_minutes(dob):
    age_in_seconds = relativedelta(date.today(), dob).seconds
    age_in_minutes = round(age_in_seconds / 60)
    return age_in_minutes


def convert_to_words(number):
    if number == 0:
        return "zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if number < 20:
        return ones[number]
    elif number < 100:
        return tens[number // 10] + (" " + ones[number % 10] if number % 10 != 0 else "")
    elif number < 1000:
        return ones[number // 100] + " hundred" + (" " + convert_to_words(number % 100) if number % 100 != 0 else "")
    elif number < 1000000:
        return convert_to_words(number // 1000) + " thousand" + (
            " " + convert_to_words(number % 1000) if number % 1000 != 0 else "")
    elif number < 1000000000:
        return convert_to_words(number // 1000000) + " million" + (
            " " + convert_to_words(number % 1000000) if number % 1000000 != 0 else "")
    else:
        return "number too large"


if __name__ == "__main__":
    main()
