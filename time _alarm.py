import schedule, time
import pygetwindow as pgw
import pyautogui as pag
from datetime import datetime
    

# print(time())
print(datetime.now())
print(datetime.time(datetime.now())) 

now= datetime.now()
print(now.strftime("%x")) 
print(now.strftime("%c")) 

print(now.strftime("%X")) 

while True:
    now= datetime.now()

    if now.strftime("%X") ==  '11:38:55'  :
        print('gxchjc')
        break
    else:
        print(now.strftime("%X"))    