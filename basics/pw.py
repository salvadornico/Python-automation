#! python3
# pw.py - an insecure password locker

import sys
import pyperclip

PASSWORDS = {
	'gh': {
		'password': 'REDACTED',
		'name': 'Github'
	},
	'bb': {
		'password': 'REDACTED',
		'name': 'Work Bitbucket'
	}
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copies account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account]['password'])
    print('Password for ' + PASSWORDS[account]['name'] + ' copied to clipboard.')
else:
    print('No account for ' + PASSWORDS[account]['name'] + ' found.')
