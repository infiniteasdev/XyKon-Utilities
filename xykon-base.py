import os
import sys
import time
from utils.stuff import logo

try:
    import pystyle
    import asyncio
    import logging
    import colorama
    import aiohttp
    import json
except Exception as e:
    print("ERROR: Run using run.bat.\n")
    input("Press any key to exit.")

p1 = colorama.Fore.MAGENTA
w1 = colorama.Fore.WHITE
e1 = colorama.Fore.CYAN
zx = f"{p1}XYKON{w1} >> "


def waitscrn():
    print(pystyle.Center.XCenter(p1 + logo + w1))

    try:
        with open('xykon-config.json') as f:
            cfg = json.load(f)
            ctoken = cfg["token"]
        print("Loaded")
        print(ctoken)
        input("")
    except FileNotFoundError as e:
        print("\n")
        print(f"{zx}ERROR: Config file not found.")
        time.sleep(1)
        print(f"{zx}Creating new config file with the name {e1}xykon-config.json{w1}")
        print(f"{zx}Make sure Xykon is in a folder of its own.")
        time.sleep(1)
        print(f"{zx}Enter your token for the config file.")
        tkn = input(f"{p1}> ")
        writecfg = {
            "token": f"{tkn}",
        }
        conf = json.dumps(writecfg)
        with open("xykon-config.json", "w") as jsonfile:
            jsonfile.write(conf)


waitscrn()
