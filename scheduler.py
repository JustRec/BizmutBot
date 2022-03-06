import schedule
import time
from threading import Thread

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
    updater.bot.send_message(chat_id=1467840078, text="I'm a bot, please talk to me!")


def __Schedule_Starter(): #Start the scheduler at .00 or .30
    
    schedule.every().day.at("18:00").do(__Job)
    Thread(target=__Schedule_Checker).start()

def Scheduler(Updater,Cursor):
    global updater, cursor
    updater = Updater
    cursor = Cursor
    
    Thread(target=__Schedule_Starter).start()

if __name__ == "__main__":
    Scheduler()