#! Python3
# pw.py  -  An insecure psw locker program.

PSW = {'email': 'dsnaknNKmlkkmolnJKJLK',
       'BLOG': 'HKJhjkJKJLKJLHGFYG',
       'luggage': '12345'}

import sys

if len(sys.argv) < 2:
    print('Usage: pthon pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name
