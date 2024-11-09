import re

def formatDate(text):
    pattern = r"(\d{1,2})[\/-](\d{1,2})[\/-](\d{2,4})"
    x = re.search(pattern, text)
    day, month, year = x.groups()
    if ((len(day)<2) and len(month)<2):
        day = '0' + day
        month = '0' + month
    elif (len(day)<2):
        day = '0' + day
    elif (len(month)<2):
        month = '0' + month
    else:
        pass
    if (len(year)==2):
        year = '20' + year
    else:
        pass
    return (day+'/'+month+'/'+year)

text = """
The event dates are the follows
- 08-07-2024
- 9/07/2024
- 11-7-2024
- 11/01/2024
- 1/07/24
"""

pattern = r"\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4}"
f = re.findall(pattern, text)
result = re.sub('08-07-2024', formatDate('08-07-2024'), text)
for match in f:
    print (match)
    text = re.sub(match, formatDate(match), text)
print(text)