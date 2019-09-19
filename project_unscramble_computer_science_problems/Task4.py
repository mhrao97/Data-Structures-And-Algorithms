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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = []
maybe_telemarketer = None

for i in range(len(calls)):
    maybe_telemarketer = calls[i][0]
    for j in range(len(calls)):
        if calls[j][1] == maybe_telemarketer:
            maybe_telemarketer = None
            break
    for j in range(len(texts)):
        if texts[j][0] == maybe_telemarketer:
            maybe_telemarketer = None
            break

    if not (maybe_telemarketer == None):
        if maybe_telemarketer not in telemarketers:
            telemarketers.append(maybe_telemarketer)

sorted_result = sorted(telemarketers)
print("These numbers could be telemarketers:")
for i in range(len(sorted_result)):
    print(sorted_result[i])
