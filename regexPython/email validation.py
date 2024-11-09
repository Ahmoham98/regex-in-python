import re

text = input("Type your email here please: ")
pattern1 = r"@"
pattern2 = r".com$"

x = re.search(pattern1, text)
y = re.search(pattern2, text)

if x and y:
    print ("YES!!, This is an email")
else:
    print("NO!!, This is not an email")  # Output: YES!!, This is an
