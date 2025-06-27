import re

# A strong password has several rules:
# - It must be at least 8 characters long
# - It must contain both uppercase and lowercase letters
# - And it must have at least one digit
#
def validate_password(password):
    len_re       = re.compile(r".{8,}")
    lowercase_re = re.compile(r"[a-z]")
    uppercase_re = re.compile(r"[A-Z]")
    digit_re     = re.compile(r"\d")

    errors = []

    if not len_re.search(password):
        errors.append("Password too short.")
    if not lowercase_re.search(password):
        errors.append("Must include at least one lowercase character.")
    if not uppercase_re.search(password):
        errors.append("Must include at least one uppercase character.")
    if not digit_re.search(password):
        errors.append("Must include at least one number.")
    
    if errors:
        for error in errors:
            print(error)
        return False

    print("Password is secure!")
    return True

password = "fdffD6t.b#"
validate_password(password)