from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import sqlite3
from scheduler import scheduler
from dotenv import load_dotenv


#Connect to the database and create a table if doesn't exist
con = sqlite3.connect('database.db', check_same_thread=False)
cursor = con.cursor()
cursor.execute('create table if not exists USERS (ID INT PRIMARY KEY, TLG_ID INT, TOKEN INT, FREQ)')
con.commit()

#Set up the connection to the telegram
load_dotenv()
updater = Updater(os.getenv('KEY'), use_context=True) 
dispatcher = updater.dispatcher

def Start(update, context):
    is_it_new_user = True
    update.message.reply_text("BizmutBot'a Hoşgeldin ヾ(ﾟ∀ﾟゞ)")
    
    #Find if the user has opened an account before
    check = cursor.execute("SELECT tlg_id from USERS")
    for row in check:
        if row[0] == update.message.from_user.id:
            is_it_new_user = False
            break
    
    row = len(cursor.fetchall())
    if is_it_new_user: # Create a row with user values in USERS table
        update.message.reply_text("Lütfen /aralik [sayı] komutunu kullanarak bildirim alma sıklığını ayarla ヽ(^。^)丿")
        update.message.reply_text("(1, 5, 10 ya da 15)")
        cursor.execute(f"INSERT INTO USERS (ID, TLG_ID, TOKEN, FREQ) \
        VALUES ({len(cursor.fetchall()) + 1}, {update.message.from_user.id}, 0, 0)")
        con.commit()
    else:
        update.message.reply_text("Kalan süre: ")

def frequency(update, context):
    freq = int(update.message.text[8:])
    cursor.execute(f"UPDATE USERS set FREQ = {freq} where TLG_ID = {update.message.from_user.id}")
    con.commit()

    update.message.reply_text(f"Bildirim gönderme sıklığı günde {freq} olarak ayarlandı")

updater.dispatcher.add_handler(CommandHandler('start', Start))
updater.dispatcher.add_handler(CommandHandler('aralik', frequency))



scheduler()
updater.start_polling()
updater.idle()