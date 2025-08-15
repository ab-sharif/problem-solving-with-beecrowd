n = int(input())

for i in range(n):
    number = input().strip()

    if len(number) != 8:
        print("FAILURE")
        continue

    if not (number[0].isupper() and number[1].isupper() and number[2].isupper()):
        print("FAILURE")
        continue

    if number[3] != '-':
        print("FAILURE")
        continue

    if not(number[4].isdigit() and number[5].isdigit() and number[6].isdigit() and number[7].isdigit()):
        print("FAILURE")
        continue

    last_digit = number[7]

    if last_digit == "1" or last_digit == "2":
        print("MONDAY")
    elif last_digit == "3" or last_digit == "4":
        print("TUESDAY")
    elif last_digit == "5" or last_digit == "6":
        print("WEDNESDAY")
    elif last_digit == "7" or last_digit == "8":
        print("THURSDAY")
    elif last_digit == "9" or last_digit == "0":
        print("FRIDAY")