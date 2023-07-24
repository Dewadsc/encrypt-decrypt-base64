import os
import base64

s = open("main.py").read()
b = base64.b64encode(s.encode('ascii'))

w = open('hasilEncryptBase64.py', 'w')
w.write('import base64\n')
w.write('exec(base64.b64decode('+repr(b)+'))')
w.close()