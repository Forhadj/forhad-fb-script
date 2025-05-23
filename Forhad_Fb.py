#!/usr/bin/env python3
# FORHAD Facebook Cracking Tool - Full Version
# Version 1.0 | Created by Forhad Hasan (SSB Team)

import os
import sys
import time
import random

# Output directory
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Custom FORHAD ASCII Logo
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[1;36m')
    print(r"""
`7MM"""YMM   .g8""8q. `7MM"""Mq.  `7MMF'  `7MMF'      db      `7MM"""Yb.
  MM    `7 .dP'    `YM. MM   `MM.   MM      MM       ;MM:       MM    `Yb.
  MM   d   dM'      `MM MM   ,M9    MM      MM      ,V^MM.      MM     `Mb
  MM""MM   MM        MM MMmmdM9     MMmmmmmmMM     ,M  `MM      MM      MM
  MM   Y   MM.      ,MP MM  YM.     MM      MM     AbmmmqMA     MM     ,MP
  MM       `Mb.    ,dP' MM   `Mb.   MM      MM    A'     VML    MM    ,dP'
.JMML.       `"bmmd"' .JMML. .JMM..JMML.  .JMML..AMA.   .AMMA..JMMmmmdP'
          FB Login Tool | Version 1.0
        Created by Forhad Hasan
""")
    print('\033[0m')

# Random User-Agent
def rand_ua():
    model = random.choice(["Nokia", "Samsung", "Infinix", "Techno", "Vivo", "Realme", "Xiaomi"])
    ver = f"{random.randint(10,13)}"
    build = f"QP1A.{random.randint(111111,999999)}.{random.randint(100,999)}"
    return f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/{build})"

# Placeholder methods
def methodA():
    logo()
    print("[Method A] File crack - under construction.")
    input("Press Enter to go back...")

def methodB():
    logo()
    print("[Method B] UID + passlist crack - under construction.")
    input("Press Enter to go back...")

def methodC():
    logo()
    print("[Method C] Dumped UID crack - under construction.")
    input("Press Enter to go back...")

def methodD():
    logo()
    print("[Method D] Cookie-based login - under construction.")
    input("Press Enter to go back...")

# Contact Developer
def contact_developer():
    logo()
    print("Contact Developer:")
    print("[1] Facebook")
    print("[2] GitHub")
    print("[3] Telegram")
    print("[4] YouTube")
    print("[0] Back")
    opt = input("\nSelect: ")
    if opt == '1':
        os.system("xdg-open https://facebook.com/forhadhasan995")
    elif opt == '2':
        os.system("xdg-open https://github.com/Forhadj")
    elif opt == '3':
        os.system("xdg-open https://t.me/f_forhad")
    elif opt == '4':
        os.system("xdg-open https://youtube.com/@forhad2.00?si=vmV-oUKHLF3ZCTnu")
    elif opt == '0':
        menu()
    else:
        print("Invalid."); time.sleep(1); contact_developer()

# Main Menu
def menu():
    logo()
    print("Select an option:")
    print("[1] Crack - Method A (File UID|Name)")
    print("[2] Crack - Method B (UID only + PassList)")
    print("[3] Crack - Method C (Dumped IDs)")
    print("[4] Crack - Method D (Cookie Login)")
    print("[5] Contact Developer")
    print("[0] Exit")
    choice = input("\nEnter choice: ")

    if choice == '1':
        methodA()
    elif choice == '2':
        methodB()
    elif choice == '3':
        methodC()
    elif choice == '4':
        methodD()
    elif choice == '5':
        contact_developer()
    elif choice == '0':
        print("Exiting..."); time.sleep(1); sys.exit()
    else:
        print("Invalid option."); time.sleep(1); menu()

# Start the tool
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
