from time import time
import hashlib


def isRequestOK(key):
    if(key):
        keyId = 'qwerty13579'
        now = int(time())
        keyArr = key.split('-')
        validString = keyId+keyArr[1]
        validHash = hashlib.sha256(validString.encode()).hexdigest()
        return not (now - int(keyArr[1]) > 300 or keyArr[0] != validHash)
    else:
        return False
