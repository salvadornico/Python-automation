import re

phoneNumRegex = re.compile(r'''(\d{3,4}     # optional area code or cell prefix
                               (-|\s|\.)?)? # separator, must follow previous grouping
                               (\d{3})      # first 3 digits
                               (-|\s|\.)?   # separator
                               (\d{4})      # last 4 digits
                               ''', re.VERBOSE)

emailRegex = re.compile(r'''([a-zA-Z0-9._]+)# username
                            (@\w+\.\w+)     # @domain + TLD
                            (\.\w\w)?       # optional country code
                            ''', re.VERBOSE)

def hasPhone(message):
    mo = phoneNumRegex.findall(message)
    if len(mo) == 0:
        print("No phone numbers found.")
    else:
        print("Phone numbers found: ")
        for i in range(len(mo)):
            for j in range(len(mo[i])):
                print(mo[i][j], end="")
            print()

def hasEmail(message):
    mo = emailRegex.findall(message)
    if len(mo) == 0:
        print("No email addresses found.")
    else:
        print("Email addresses found: ")
        for i in range(len(mo)):
            for j in range(len(mo[i])):
                print(mo[i][j], end="")
            print()

print("Type in your string: ")
evalString = input()
hasPhone(evalString)
hasEmail(evalString)
