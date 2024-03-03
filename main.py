import requests
import random
import time

url = "find this on inspect element "

headers = {
    "Authorization" : "Find this in inspect element"
}


def task():
    amount  = random.randint(1,9)*10 

    saying = "dam im up " + str(amount)
    string_list = ["sold","damn", "plays selling", "everything selling" , "why is everyone selling" , saying ,"idk how im goin down bettin on promos","idrk what to send just trying to send a messsage to get my level up :)"]
    payload = {
        "content": random.choice(string_list)
    }
    res = requests.post(url,payload,headers=headers)
    return res


while True:
    task()
    time.sleep(random.randint(2,8))