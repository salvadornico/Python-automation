#! python3
# Launches a Google search for a given name's Facebook, Twitter, and Instagram from either command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Gets string from command line argument
    name = ' '.join(sys.argv[1:])
else:
    # Get string from clipboard
    name = pyperclip.paste()

webbrowser.open('https://www.google.com.ph/search?q=' + name + '+instagram')
webbrowser.open('https://www.google.com.ph/search?q=' + name + '+facebook')
webbrowser.open('https://www.google.com.ph/search?q=' + name + '+twitter')