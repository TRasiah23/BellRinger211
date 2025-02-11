import time
local= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
a=15
b=24
c=00
result=(a-"%H",":",b-"%M",":",c-"%S")
print(result)
