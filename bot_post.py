from instabot import Bot 
import time, os, random  
  
bot = Bot() 

contas = [
    'userprofile01',
]

    
for conta in contas:
    bot.login(username = conta,  
            password = "instagramPassword") 
    for i in range(0, 6):
        time.sleep(5)
        photo = ('img/yourImageName ({}).jpg'.format(random.randint(2,34)))
        bot.upload_photo(photo, caption = "") 
        time.sleep(2)
        path_remove = '{}.REMOVE_ME'.format(photo)
        time.sleep(2)
        os.rename(src = path_remove, dst = photo)
   
        
    