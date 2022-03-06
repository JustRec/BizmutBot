import schedule
import time
from threading import Thread

def __IsItNotifTime():
    sys_time = int(time.ctime(time.time())[11:13] + time.ctime(time.time())[14:16] ) #Hour and minute value in local time
    print(f"Notification check at: {sys_time}")

    return sys_time != 1000 and sys_time != 1300 #Remove 2 time to make total notif count to 15

def __Schedule_Checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

def __Freq_Flag():
    flag = 15
    hour = int(time.ctime(time.time())[11:13])

    exc_times_10 = [12, 14, 15, 16, 17]
    for i in exc_times_10:
        if i == hour:
            flag = 5
            break
    
    return flag
    


def __Job():
    if __IsItNotifTime():
        print("its working")

    updater.bot.send_message(chat_id=1467840078, text="I'm a bot, please talk to me!")


def __Schedule_Starter(): #Start the scheduler at .00 or .30
    while int(time.ctime(time.time())[14:16]) != 00 and int(time.ctime(time.time())[14:16]) != 30:
        time.sleep(1)
    
    schedule.every(5).seconds.do(__Job)
    Thread(target=__Schedule_Checker).start()

def Scheduler(Updater,Cursor):
    global updater, cursor
    updater = Updater
    cursor = Cursor
    
    Thread(target=__Schedule_Starter).start()

if __name__ == "__main__":
    Scheduler()