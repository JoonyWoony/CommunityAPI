import requests
import json

test_usernames = {0: "56ms", 1: "nonbunary", 2: "poroknights",
                  3: "UrMinecraftDoggo", 4: "Skezza", 5: "kori_100",
                  6: "XD_Zaptro_XD", 7: "seattle72", 8: "Refraction"}

user = 0
username = test_usernames[user]

API_KEY = ""


#a = requests.get("https://api.hypixelskyblock.de/api/v1/cb/pages/balt")

#username = "ycarusishere"
#username = "KebabOnNaan"
#username = "ItzAlpha__"
#username = "balt"
#username = "455fcc3f87ea4a92a6c38e190c39d8ec"
username = "56ms"
#username = "Refraction"
#username = "seattle72"
#username = "Skezza"
#username = "laachs"

ip = "127.0.0.1"  #  For running locally
#ip = "db.superbonecraft.dk"  # For the server

#API_KEY = "Jeff"
#username="Jeffaaaaaa"

#a = requests.get(f"http://{ip}:8000/pages/{username}?api_key={API_KEY}")
a = requests.get(f"http://{ip}:8000/total/{username}?api_key={API_KEY}")

print(a.status_code)
print(a.json())
