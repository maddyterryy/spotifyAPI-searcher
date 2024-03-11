from dotenv import load_dotenv
#import os module to provide functions that interact with the operating system
import os

#this function reads the environment variables from the .env file
load_dotenv()


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)