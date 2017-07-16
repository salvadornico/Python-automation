#! python3
# pw.py - an insecure password locker

import sys
import pyperclip

PASSWORDS = {'email': 'my_email',
             'blog': 'my_blog',
             'suitcase': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copies account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('No account for ' + account + ' found.')
