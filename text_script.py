from pyrogram import Client, filters 
import time
import os 
api_id=    #your API_ID
api_hash="Your API hash"
Sessionstring="Your Sessionstring"
# to get Sessionstring visit https://replit.com/@ErichDaniken/Generate-Telegram-String-Session 
app = Client('your_name',       #Update this line with your name
               api_id= api_id,     #your API_ID
               api_hash=api_hash,   #your API_HASH
               session_string=Sessionstring,) #your Sessionstring
               
async def main():
    async with app:
        while True:
         await app.send_message(update your chat_id, "text here", reply_to_message_id=message_id) #to reply
         await app.send_message(update your chat_id, "text here" ) # to send plain text
         time.sleep(20)

app.run(main())

