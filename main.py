import requests
import random
import threading
import time
import os
import sys
from bs4 import BeautifulSoup

Valid = 0
Invalid = 0
Type = "PNG"

if os.path.exists("logs.log"):
    os.remove("logs.log")
open("logs.log", "w+")
if not os.path.exists("images"):
    os.mkdir("images")

session = requests.Session()
lock = threading.Lock()

def log(text, type="log"):
    with open("logs.log", "a") as logfile:
        logstring = "[" + time.strftime("%H:%M:%S") + "] " + text
        logfile.write(logstring + "\r")

    if type == "log":
        print("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m " + text)
    elif type == "error":
        print("\033[1;37m[\033[1;31mERROR\033[1;37m]\033[1;37m " + text)
    elif type == "success":
        print("\033[1;37m[\033[1;32mSUCCESS\033[1;37m]\033[1;37m " + text)

def update_title():
    global Valid
    global Invalid
    global Type

    while True:
        os.system("title Imgur Image Brute Forcer by @DRQSuperior - Valid: " + str(Valid) + " - Invalid: " + str(Invalid) + " - Type: " + Type)
        time.sleep(0.1)

def get_image():
    global Valid
    global Invalid
    global Type

    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    random_string = "".join(random.choice(CHARSET) for _ in range(7))
    try:
        # brute force imgur images
        url = "https://i.imgur.com/" + random_string + "." + Type
        r = session.get(url, allow_redirects=True)
        img = r.content
        if r.url == "https://i.imgur.com/removed.png":
            with lock:
                Invalid += 1
                update_title()
            log("Invalid image: " + url, "error")
        else:
            with lock:
                Valid += 1
                open("images/" + random_string + "." + Type, "wb").write(img)
                update_title()
            log("Valid image: " + url, "success")
            
    except:
        log("Missed image: " + url)

def main():
    global Type

    print("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m Imgur Image Brute Forcer by \033[1;31m@DRQSuperior\033[1;37m")

    Type = input("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m What type of image do you want to brute force? (PNG, JPG, JPEG, GIF, WEBP, CUSTOM) ").upper()

    if Type == "CUSTOM":
        Type = input("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m What extension do you want to brute force? (Example: PNG) ").upper()
    elif Type in ["JPG", "JPEG", "WEBP", "GIF", "PNG"]:
        Type = Type
    else:
        log("Invalid image type, exiting...", "error")
        sys.exit()
    Type = Type.lower()
    
    while True:
        for _ in range(100):
            threading.Thread(target=get_image).start()

        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            log("Keyboard Interrupt detected, exiting...")
            sys.exit()
    
if __name__ == "__main__":
    main()
