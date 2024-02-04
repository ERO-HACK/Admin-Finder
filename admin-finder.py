from requests import get
from colorama import init,Fore
import time
init()

time.sleep(2.5)

print ("""
    _       _           _         _____ _           _
   / \   __| |_ __ ___ (_)_ __   |  ___(_)_ __   __| | ___ _ __ 
  / _ \ / _` | '_ ` _ \| | '_ \  | |_  | | '_ \ / _` |/ _ \ '__|
 / ___ \ (_| | | | | | | | | | | |  _| | | | | | (_| |  __/ |   
/_/   \_\__,_|_| |_| |_|_|_| |_| |_|   |_|_| |_|\__,_|\___|_| 
       
                                 | Developed by ERO-HACK
                                 | Telegram @EroHack0
                                 | Version : 1.0.0
""")

site = input("Enter a Target Site Url : ")
site = "http://"+site
Urls = input("Enter a Urls File : ")

time.sleep(1.5)

Urls = open(Urls,"r").read().splitlines()

for url in Urls:
    full_address = site+"/"+url
    respons = get(full_address)
    if respons.status_code == 200:
        print(f" {Fore.GREEN} {full_address} is Exsists =====> 200 {Fore.RESET}")
    else:
        print(f" {Fore.RED} {full_address} Not Found ! =====> 400 {Fore.RESET}")

