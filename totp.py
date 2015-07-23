# coding: utf-8

"""
TOTP: Time-Based One-Time Password Algorithm

https://tools.ietf.org/html/rfc6238.html
"""

import os
import sys
import time
import webbrowser

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor import InvalidToken

import pyqrcode


key = os.urandom(16)
counter = 1
time_value = time.time()
issuer = 'GruPyPR'
account_name = input('Your name: ')

totp = TOTP(key, 6, SHA1(), 30, backend=default_backend())

uri = totp.get_provisioning_uri(account_name, issuer)
url = pyqrcode.create(uri)

print('Scan this!\n')
url.svg('totp.svg', scale=8)
webbrowser.open('totp.svg')

while True:
    try:
        totp_value = bytes(input('Two factor password: '), encoding='utf-8')
        totp.verify(totp_value, time.time())
        print('You are authenticated!\n')
    except InvalidToken:
        print('You shall not pass!')
        continue
    except KeyboardInterrupt:
        sys.exit(0)
