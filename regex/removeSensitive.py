import re

sensitive_re  = re.compile(r'\d{4} \d{4} \d{4} \d{4}|\d{3}-\d{2}-\d{4}')
# ssn_re = re.compile(r'\d{3}-\d{2}-\d{4}')

test_text = "Hello, my credit card number is 4474 5204 3349 2491 and my other cc number is . Buy somethin nice! My social is 508-45-8620! Take out a loan in my name!"

censored_text = sensitive_re.sub("CENSORED", test_text)

print(censored_text)