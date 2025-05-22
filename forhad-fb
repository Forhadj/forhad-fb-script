#!/usr/bin/python
# Script by Forhad Hasan

import os
import sys
import re
import uuid
import time
import json
import random
import base64
import requests
from concurrent.futures import ThreadPoolExecutor

# Clear screen
os.system('clear')

# Define logo
logo = '''\033[1;37m
   _____             _               _               
  |  ___|           | |             | |              
  | |_ ___  _ __ ___| |__   __ _ ___| |__   ___ _ __ 
  |  _/ _ \| '__/ _ \ '_ \ / _` / __| '_ \ / _ \ '__|
  | || (_) | | |  __/ |_) | (_| \__ \ | | |  __/ |   
  \_| \___/|_|  \___|_.__/ \__,_|___/_| |_|\___|_|   
----------------------------------------------------
 Owner   : Forhad Hasan
 Facebook: https://www.facebook.com/forhadhasan995
 GitHub  : https://github.com/Forhadj
 Telegram: @f_forhad
 Version : 1.0
----------------------------------------------------'''

# Show logo
print(logo)

# Check and install missing modules
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize')
    import mechanize

# Random user-agent builder
model2 = ["Nokia", "Samsung", "Infinix", "Techno", "Vivo"]

def rand_user_agent():
    version = f"{random.randint(100,999)}.0.0.{random.randint(1,9)}.{random.randint(40,150)}"
    build = f"QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}"
    android_ver = random.randint(5,13)
    model = random.choice(model2)
    return f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/{build})"

# Example login function

def login_facebook(uid, password):
    session = requests.Session()
    headers = {
        'User-Agent': rand_user_agent(),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com'
    }
    data = {
        "adid": str(uuid.uuid4()),
        "email": uid,
        "password": password,
        "credentials_type": "device_based_login_password",
        "source": "device_based_login",
        "format": "json",
        "generate_session_cookies": "1",
        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
        "method": "auth.login",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d"
    }
    try:
        response = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers)
        result = response.json()
        if 'session_key' in result:
            print(f"[OK] {uid} | {password}")
        elif 'error' in result and 'www.facebook.com' in result['error'].get('message', ''):
            print(f"[CP] {uid} | {password}")
        else:
            print(f"[FAIL] {uid} | {password}")
    except Exception as e:
        print(f"[ERROR] {uid} | {password} => {e}")

# Main function

def main():
    print("\n[1] Try a sample login")
    print("[0] Exit")
    choice = input("Select option: ")
    if choice == '1':
        uid = input("Enter UID/Email: ")
        password = input("Enter Password: ")
        login_facebook(uid, password)
    else:
        print("Exiting...")
        sys.exit()

# Run the main menu
if __name__ == '__main__':
    main()
