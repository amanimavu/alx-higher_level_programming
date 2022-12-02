#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_value = number * -1 if number < 0 else number
last_digit = (abs_value % 10) * -1 if number < 0 else (abs_value % 10)
statement_for_greater5 = "Last digit of {} is {} and is greater than 5"
statement_for_0 = "Last digit of {} is {} and is 0"
statement_for_less6 = "Last digit of {} is {} and is less than 6"

if last_digit > 5:
    print(statement_for_greater5.format(number, last_digit))
elif last_digit == 0:
    print(statement_for_0.format(number, last_digit))
else:
    print(statement_for_less6.format(number, last_digit))
