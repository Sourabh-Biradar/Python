# datetime library

import datetime

t = datetime.datetime.now()
print(t)

t1 = datetime.datetime(1996,2,15)
print(t1.strftime("%A"))
print(t1.strftime("%b"))
print(t1.strftime("%y"))