import pywhatkit

# Send message to a contact
phone_number = input('Enter phone number with country code: ')

# message = 'Test', time(hrs) = 7, time(mins) = 21
pywhatkit.sendwhatmsg(phone_number, 'Test', 7, 21)
# message = 'Test', time(hrs) = 7, time(mins) = 25, wait time = 15 secs, window close = true, close time = after 2 seconds
pywhatkit.sendwhatmsg(phone_number, 'Test', 7, 25, 15, True, 2)

# Send message to a group
group_id = input('Enter group id: ')

pywhatkit.sendwhatmsg_to_group(group_id, 'Test Group', 7, 31)
