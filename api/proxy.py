import jwt
import time
s = jwt.encode({'user':'luo','exp':time.time()+3},'12345',algorithm='HS256')
print(s)
time.sleep(2)
j = jwt.decode(s,'12345',algorithms="HS256")
print(j)

