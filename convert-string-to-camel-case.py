import re

def to_camel_case(text):
    arr = re.split('-|_', text)
    return arr[0] + ''.join(x.capitalize() for x in arr[1:])


print(to_camel_case("the-stealth-warrior"))