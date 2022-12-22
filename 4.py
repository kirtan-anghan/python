import time
ctime=time.strftime("%H:%M:%S")
htime=time.strftime('%H')
mtime=time.strftime('%M')
stime=time.strftime('%S')

if(htime >= "0" and htime<="12"):
   print("good morning sir!!")
elif(htime >'12' and htime <'18'):
    print("good afternoon sir!!")
else:
    print("good night sir!!")
