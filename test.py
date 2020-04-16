
from FBAuto import autofb
import sys
import base64
import json
import time
#enter command
for index in range(1, len(sys.argv)):

    if sys.argv[index] == '-credit': 
        message_bytes = base64.b64decode(sys.argv[index + 1])
        message = message_bytes.decode('ascii')
        creditCard = json.loads(message)
    if sys.argv[index] == '-acc':

        message_bytes = base64.b64decode(sys.argv[index + 1])
        message = message_bytes.decode('ascii')
        account = json.loads(message)
fb = autofb()

fb.login(account, 'cookie')
if fb.checkLogin():
    fb.addAds()
    print('success')
else:
    print('error')
    
time.sleep(10000)