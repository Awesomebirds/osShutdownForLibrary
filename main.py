import os
from pytimekr import pytimekr
from datetime import datetime

def is_holiday():
    #휴일 체크 (월요일 또는 공휴일)
    
    if datetime.now().weekday()==0 or datetime.now().date() in pytimekr.holidays():
        return True
    else:
        return False

def system_shutdown(): os.system("shutdown -s -t 60")

if is_holiday(): system_shutdown()