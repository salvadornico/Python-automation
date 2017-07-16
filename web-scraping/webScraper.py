#! python3
# Launches a Google Maps search from either command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Gets string from command line argument
    address = ' '.join(sys.argv[1:])
else:
    # Get string from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)