from time import time
import hashlib


def isRequestOK(key):
    if(key):
        keyId = 'qwerty13579'
        now = int(time())
        keyArr = key.split('-')
        validString = keyId+key[1]
        validHash = hashlib.sha256(validString.encode()).hexdigest()
        return not (now - int(key[1]) > 10 or key[0] != validHash)
    else:
        return False
