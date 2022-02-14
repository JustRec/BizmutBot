import schedule
import time
from threading import Thread


def __IsItNotifTime():
    sys_time = int(time.ctime(time.time())[11:13] + time.ctime(time.time())[14:16] ) #Hour and minute value in local time
    print(f"Notification check at: {sys_time}")

    return sys_time != 1000 and sys_time != 1300 #Remove 2 time to make total notif count to 15

def __schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

def __job():
    if __IsItNotifTime():
        print("its working")

def __schedule_starter(): #Start the scheduler at 00 or 30
    while int(time.ctime(time.time())[14:16]) != 00 and int(time.ctime(time.time())[14:16]) != 30:
        time.sleep(1)
    
    schedule.every(30).minutes.do(__job)
    Thread(target=__schedule_checker).start()

def scheduler():
    Thread(target=__schedule_starter).start()

if __name__ == "__main__":
    scheduler()