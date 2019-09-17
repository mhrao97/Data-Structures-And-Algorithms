"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

calls_from_bangalore = []
calls_to_fixed_lines = []
calls_to_number = []
codes = []
calls_to_bangalore_fixed_lines = []
from_fixed = 0
to_fixed = 0
to_fixed_bangalore = 0

print("The numbers called by people in Bangalore have codes:")
for i in range(len(calls)):
    if calls[i][0].startswith("(080)"):
        bangalore_number = calls[i][0]
        from_fixed += 1
        if calls[i][1].startswith("(080)"):
            called_bangalore_number = calls[i][1]
            to_fixed += 1
            to_fixed_bangalore += 1
            if called_bangalore_number not in calls_to_bangalore_fixed_lines:
                calls_to_bangalore_fixed_lines.append(called_bangalore_number)
        if calls[i][1].startswith("(0"):
            to_fixed += 1
            number_called = ((calls[i][1]).replace("(", "")).replace(")", " ")
        else:
            number_called = calls[i][1]

        if bangalore_number not in calls_from_bangalore:
            calls_from_bangalore.append(bangalore_number)
        if number_called not in calls_to_number:
            calls_to_number.append(number_called)
            if number_called.startswith("0"):
                number_code = number_called.split(" ", 1)[0]
            else:
                number_code = number_called[:4]
            if number_code not in codes:
                codes.append(number_code)

print("\n".join(sorted(set(codes))))

percent_from_fixed_to_fixed = (to_fixed_bangalore / from_fixed) * 100

print("%s percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore." %(str(round(percent_from_fixed_to_fixed, 2))))