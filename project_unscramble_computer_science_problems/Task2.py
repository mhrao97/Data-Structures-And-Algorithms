"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_details = {}

for call in calls:
    if call[0] not in call_details:
        call_details[call[0]] = 0
    if call[1] not in call_details:
        call_details[call[1]] = 0

    call_details[call[0]] += int(call[3])
    call_details[call[1]] += int(call[3])

longest_time_caller = max(call_details, key=call_details.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_time_caller, \
                                                                                          call_details[
                                                                                              longest_time_caller]))
