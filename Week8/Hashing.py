import hashlib
m = hashlib.md5()
m.update('str'.encode('utf-8'))
m.update('abc')