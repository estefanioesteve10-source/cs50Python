import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    start = to_24(int(h1), int(m1) if m1 else 0, p1)
    end = to_24(int(h2), int(m2) if m2 else 0, p2)

    return f"{start} to {end}"


def to_24(hour, minute, period):
    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour")

    if minute < 0 or minute > 59:
        raise ValueError("Invalid minute")

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
