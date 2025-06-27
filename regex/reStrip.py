import re

def re_strip(string, remove=None):
    if remove:
        to_remove = re.compile(f"[{re.escape(remove)}]")
        return to_remove.sub("", string)
    else:
        strip_re = re.compile(r'(^\s+)?(\s+$)?')
        return strip_re.sub("", string)

test_string = "\n\n\t  \t Hello planet!! \t\t  \n"

print(re_strip(test_string))
print(re_strip(test_string, "aeiou\t\n Hello planet"))


