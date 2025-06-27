#
# is_phone_number(text): checks if a given string of text is a phone number in the format of
#                        999-999-9999
#
def is_phone_number(text):
    if len(text) != 12:    # Phone numbers have 12 characters, so if it is not of length 12, it can be automatically eliminated
        return False
    
    for i in range(0, 3):  # Check if first three characters are numbers
        if not text[i].isdecimal():
            return False
    
    if text[3] != "-":     # Fourth character must be a dash
        return False
    
    for i in range(4, 7):  # Check if next set of 3 are numbers
        if not text[i].isdecimal():
            return False
    
    if text[7] != "-":     # Eighth character must be a dash
        return False
    
    for i in range(8, 12): # Check if final set of 4 are numbers.
        if not text[i].isdecimal():
            return False
    
    return True            # If the code has reached this point, then it has passed all of the checks, meaning it is a phone number in our proper format

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')