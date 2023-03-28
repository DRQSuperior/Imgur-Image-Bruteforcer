import requests
import json
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
else:
    open("logs.log", "w+")
if not os.path.exists("images"):
    os.mkdir("images")

def log(text, type="log"):
    logfile = open("logs.log", "a")
    logstring = "[" + time.strftime("%H:%M:%S") + "] " + text
    logfile.write(logstring + "\r")
    logfile.close()

    if type == "log":
        print("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m " + text)
    elif type == "error":
        print("\033[1;37m[\033[1;31mERROR\033[1;37m]\033[1;37m " + text)
    elif type == "success":
        print("\033[1;37m[\033[1;32mSUCCESS\033[1;37m]\033[1;37m " + text)

def get_image():
    global Valid
    global Invalid
    global Type

    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    random_string = "".join(random.choice(CHARSET) for i in range(7))
    try:
        #brute force imgur images
        url = "https://i.imgur.com/" + random_string + "." + Type
        r = requests.get(url, allow_redirects=True)
        img = r.content
        if r.url == "https://i.imgur.com/removed.png":
            log("Invalid image: " + url)
            Invalid += 1
        else:
            log("Valid image: " + url)
            Valid += 1
            open("images/" + random_string + "." + Type, "wb").write(img)
            
    except:
        log("Missed image: " + url)
        Misses += 1

def main():
    global Type

    #print banner in colors saying Imgur Image Brute Forcer by @DRQSuperior
    print("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m Imgur Image Brute Forcer by \033[1;31m@DRQSuperior\033[1;37m")

    #ask user for type of image
    Type = input("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m What type of image do you want to brute force? (PNG, JPG, JPEG, GIF, WEBP, CUSTOM) ").upper()

    #if user wants to brute force custom image type
    if Type == "CUSTOM":
        Type = input("\033[1;37m[\033[1;34mLOG\033[1;37m]\033[1;37m What extension do you want to brute force? (Example: PNG) ").upper()
    elif Type == "JPG":
        Type = "JPG"
    elif Type == "JPEG":
        Type = "JPEG"
    elif Type == "WEBP":
        Type = "WEBP"
    elif Type == "GIF":
        Type = "GIF"
    elif Type == "PNG":
        Type = "PNG"
    else:
        log("Invalid image type, exiting...", "error")
        sys.exit()


    while True:
        for i in range(100):
            threading.Thread(target=get_image).start()

        try:
            time.sleep(0.0001)
        except KeyboardInterrupt:
            log("Keyboard Interrupt detected, exiting...")
            sys.exit()
    
if __name__ == "__main__":
    main()
