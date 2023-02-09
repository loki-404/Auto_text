from pyrogram import Client, filters 
import time
import os 
api_id=20641648       #your API_ID
api_hash="008adc8089860736b3493adf49ea3c32"
Sessionstring="BQAc7_bLwJDvz1u-2NjJfnL64AJetApnjmGVHS8k-X1XRjFlGwYdNiOzkV8WBRrP_YVxOWEknThDQrIXXwwhV-O-dZ_rkCAlmLVpHP0l-KQA0WSKt6TNymqcPocXbtBMkxHu2JqlpNiLlqw5JLpngqfSKnghdHMNKGUjZOoxg5nrCtVYk42IwULbmXThVpBA7dgpg0HghnaIN2nGOZPY37EVfoSRliLuS9IIF85qReAjf7YtNWK_L85qsAQ5eO0m0VWQrj_9UJKkOxw1sQZSdEwSXegh7ACoNcnq3YkaCzz0Wi8rt8zPqdR1tRN5lP9ziYUk38Vo9rfWZNiZHJssoRMhAAAAAHHZNOUA"# Your Sessionstring
app = Client('Dexter',       #Update this line with
               api_id= api_id,     #your API_ID
               api_hash=api_hash,   #your API_HASH
               session_string=Sessionstring,) #your Sessionstring
               
async def main():
    async with app:
        while True:
         #await app.send_message(-1001676181203, "+", reply_to_message_id=2152) #to reply
         await app.send_message(-1001676181203, "/soccer 7982388" ) #plain text
         time.sleep(20)
         

app.run(main())

