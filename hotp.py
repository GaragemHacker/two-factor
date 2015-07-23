# coding: utf-8

"""
HOTP: An HMAC-Based One-Time Password Algorithm

https://tools.ietf.org/html/rfc4226.html
"""

import os
import sys
import webbrowser

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor import InvalidToken

import pyqrcode


key = os.urandom(16)
counter = 1
issuer = 'GruPyPR'
account_name = input('Your name: ')

hotp = HOTP(key, 6, SHA1(), backend=default_backend())

uri = hotp.get_provisioning_uri(account_name, counter, issuer)
url = pyqrcode.create(uri)
print('Scan this!\n')
url.svg('hotp.svg', scale=8)
webbrowser.open('hotp.svg')

while True:
    try:
        hotp_value = bytes(input('Two factor password: '), encoding='utf-8')
        hotp.verify(hotp_value, counter)
        print('You are authenticated!\n')
    except InvalidToken:
        print('You shall not pass!\n')
        continue
    except KeyboardInterrupt:
        sys.exit(0)
