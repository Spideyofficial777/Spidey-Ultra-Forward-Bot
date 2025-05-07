import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "28519661")
    API_HASH = environ.get("API_HASH", "d47c74c8a596fd3048955b322304109d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://voromil970:q9aLNL7nsD8EDzwL@cluster0.rlvax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "SPIDEY777")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5518489725').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002423451263'))
    FORCE_SUB_CHANNEL = list(map(int, getenv("FORCE_SUB_CHANNEL", "-1001959922658,-1002470391435,-1002433552221").replace(" ", "").split(",")))
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')

#starting imgs
    START_IMG = (environ.get('START_IMG', 'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg https://graph.org/file/d6d9d9b8d2dc779c49572.jpg https://graph.org/file/4b04eaad1e75e13e6dc08.jpg https://graph.org/file/05066f124a4ac500f8d91.jpg https://graph.org/file/2c64ed483c8fcf2bab7dd.jpg https://i.ibb.co/CPxdkHR/IMG-20240818-192201-633.jpg')).split()
        
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
