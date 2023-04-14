import os
os.system('title Xykon Selfbot - Star on github if you enjoy!')

import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands
import time 
from time import sleep
import aiohttp
import asyncio
import json
import colorama
import threading
from colorama import Fore, Back, Style, init
import re
import tracemalloc
import pystyle
from pystyle import Colors, Colorate, Box, Center
import requests
tracemalloc.start()

white =  Fore.WHITE
black = Fore.BLACK
red = Fore.RED
blue = Fore.CYAN
green = Fore.GREEN
ts = time.time()


logo = """
 __   ____     ___  ______  _   _ 
 \ \ / /\ \   / / |/ / __ \| \ | |
  \ V /  \ \_/ /| ' / |  | |  \| |
   > <    \   / |  <| |  | | . ` |
  / . \    | |  | . \ |__| | |\  |
 /_/ \_\   |_|  |_|\_\____/|_| \_|
          S E L F B O T
 \n"""

skull = """
       @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@
@@@@@@@@@@@@@@@@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@@@@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@|  | | | | | | | |
                 \_|_|_|_|_|_|_|_|"""

bot = commands.Bot(command_prefix="xykon", self_bot=True)
bot.remove_command(help)

#select mode
print(Center.XCenter(f"{blue}{logo}{white}\n"))
print(Center.XCenter(f"         1:  Load {green}Safe {white}Mode"))
print(Center.XCenter(f"         2: Load {red}Blatant {white}Mode"))
numchoice = int(input("Select your choice >> "))
if numchoice == 1:
    os.system("cls")
    print(f"Loading {green}Safe {white}Mode")
    safemode = True
    blatantmode = False
elif numchoice == 2:
    blatantmode = True
    safemode = False
    os.system("cls")
    input(f"[{red}XYKON{white}] Are you sure you want to load {red}Blatant {white}Mode?")
    print(f"[{red}XYKON{white}] Loading {red}Blatant {white}Mode")
    sleep(2)
    os.system("cls")
    print(Center.Center(red + skull + white + "\n"))
    sleep(5)
    
else:
    print("Enter a valid choice.")    
os.system("cls")


def sfobl():
    if blatantmode == False and safemode == True:
        print(Center.XCenter(f"{blue}{logo}{white}"))
    elif blatantmode == True and safemode == False:
        print(Center.XCenter(f"{red}{logo}{white}"))


# Loading Screen

#Print Logo and text
sfobl()
print(pystyle.Center.XCenter(Box.DoubleCube("   1: Load custom token   \n   2: Load from config   \n   3: Create a new config      ")))
choice = input(Center.XCenter("Your choice >> "))



if choice == '1':    
    os.system('cls')
    token = input("Enter your token: ")
elif choice == '2':
    try:
        os.system('cls')
        with open('config.json') as f:
            config = json.load(f)
            token1 = config['token']

        print(f'{blue}XYKON{white} >> Loading config.json..')
        with open ('config.json') as f:
            config = json.load(f)
            token1 = config['token']
            print(f'{blue}XYKON{white} >> Loaded token from config.json')
            print(f'{blue}XYKON{white} >> Attempting to login')
    except Exception as e:
        print(f"{blue}XYKON{white} >> config.json is not found on this directory. Creating one now...")
        print(f"{blue}XYKON{white} >> Enter your token to fill in the config.json file!")
        configtoken = input(f"{blue}XYKON{white} >> Enter your token: ")
        saveconfig = {
            "token": f"{configtoken}",
        }
        conf = json.dumps(saveconfig)

        with open("config.json", "w") as jsonfile:
            jsonfile.write(conf)
        print(f"{blue}XYKON{white} >> Written config.json successfully with token")
    token1 = token1

elif choice == '3': 
    os.system('cls')
    print(f"{blue}XYKON{white} >> To create your config file, Enter your token below")
    configtoken = input(f"{blue}XYKON{white} >> Enter your token: ")
    saveconfig = {
        "token": f"{configtoken}",
    }
    conf = json.dumps(saveconfig)

    with open("config.json", "w") as jsonfile:
        jsonfile.write(conf)
    print(f"{blue}XYKON{white} >> Written config.json successfully with token")



@bot.event
async def on_ready():
    print(f"{blue}XYKON{white} >> Activated Xykon for {bot.user.name}#{bot.user.discriminator}")

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, channelID, *, message):
    await ctx.message.delete()
        
    for i in range(amount): # Do the next thing amount times\
        url = f"https://discord.com/api/v9/channels/{channelID}/messages".format(channelID)
        data = {"content": message}
        header = {"authorization": token1}
        r = requests.post(url, json=data, headers=header)
        if channelID == None:
            print(f"{blue}XYKON{white} >> You have to provide a channel ID.")
        else:
            print(f"{blue}XYKON{white} >> Spam function was called for channel ID: {channelID}")


@bot.group(invoke_without_command=True)
async def help(ctx):
    if blatantmode == True and safemode == False:
        await ctx.reply("```Blatant Help command```")
    elif safemode == True and blatantmode == False:
        print("Help command:")
        
async def send_message(channelID, message):
    url = f"https://discord.com/api/v9/channels/{channelID}/messages"
    data = {"content": message}
    header = {"authorization": token1}
    r = requests.post(url, json=data, headers=header)
    await send_message()
    print(f"{blue}XYKON{white} >> Message sent to channel ID: {channelID}")

@bot.command()
async def test(ctx):
    await ctx.send("`Welcome to Xykon Selfbot`\n")

@bot.command()
async def logout(ctx):
    await ctx.message.delete()
    await ctx.send("```XYKON >> Logging out```", delete_after=1)
    await bot.close()
    print(f"{blue}XYKON{white} >> Logged out of Xykon Selfbot")
    input("Press enter to exit")

    # STUPID LOGIN SYSTEM LMFAO

if choice == '1':
    try:
        bot.run(token, bot = False)
    except Exception as e:
        print("Improper token was passed.")
        input("Restart Xykon.")
elif choice == '2':
    bot.run(token1)
else:
    pass
