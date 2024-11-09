import re
from convertdate import persian
from datetime import datetime

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
    return (year+'/'+month+'/'+day)

#send them one by one to the function to convert the data
def gregorian_to_solar_hijri(gregorian_date_str):
    # Parse the input Gregorian date string to a datetime object
    gregorian_date = datetime.strptime(gregorian_date_str, "%Y/%m/%d")
    # Convert the Gregorian date to Solar Hijri
    solar_hijri_date = persian.from_gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day)
    # Format the Solar Hijri date into YYYY/MM/DD
    return f"{solar_hijri_date[0]}/{solar_hijri_date[1]:02d}/{solar_hijri_date[2]:02d}"

text = """
The event dates are the follows
- 08-07-2024
- 9/07/2024
- 11-7-2024
- 11/01/2024
- 1/07/24
"""

#get dates from text...
pattern = r"\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4}"
matches = re.findall(pattern, text)
for Gregorian_date in matches:
    #passing Gregorian date to format it into desired format for using in Gregorian_to_solar_hijri function 
    formated_date = formatDate(Gregorian_date)
    sollar_date = gregorian_to_solar_hijri(formated_date)
    #replace them all in the main text to have sollar instead of gregorian
    text = re.sub(Gregorian_date, sollar_date, text)
    
print (text)
