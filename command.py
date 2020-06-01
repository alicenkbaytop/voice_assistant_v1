# import required modules

import webbrowser
import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html
from datetime import datetime

class Command():
    
    # cleaning words and choosing command
    def __init__(self, income_voice):
        self.voice = income_voice.upper()
        self.voice_blocks = self.voice.split()
        print(self.voice_blocks)
        self.commands = ["HAVA", "KAPAT", "NASILSIN", "SAAT"]
    
    # engine speak(saving, playing and removing sound)
    def vocalization(self, string):
        tts = gTTS(text = string, lang = "tr")
        tts.save("sound.mp3")
        playsound("sound.mp3")
        os.remove("sound.mp3")
        print(string)
    
    # KAPAT command    
    def close(self):
        self.vocalization("İyi günler dilerim...")
        sys.exit()
    
    # HAVA command    
    def weather_forecast(self):
        r = requests.get("https://www.ntvhava.com/konum/istanbul/7-gunluk-hava-tahmini")
        tree = html.fromstring(r.content)
        
        degree = tree.xpath('//*[@id="main"]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[1]/span')
        weather = tree.xpath('//*[@id="main"]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[2]')
        warning = ""
        
        if weather[0].text == "Yağmurlu":
            warning = "şemsiye almayı unutma!"
        
        string = "Bu gün hava {} ve {} gözüküyor.".format(degree[0], weather)
        self.vocalization(string)
    
    # NASILSIN command              
    def chat(self):
        sentences = ["Ben iyiyim sen nasılsın?"]    
        choice_ = choice(sentences)
        self.vocalization(choice_)
    
    # SAAT command     
    def time(self):
        print(datetime.now().strftime("%H:%M:%S"))
        self.vocalization(datetime.now().strftime("%H:%M:%S"))
    
    # matching command     
    def find_command(self):
        for command in self.commands:
            if command in self.voice_blocks:
                self.run_command(command)
    
    # and calling functions            
    def run_command(self, command):
        if command == "HAVA":
            self.weather_forecast()
            
        if command == "KAPAT":
            self.close()
            
        if command == "NASILSIN":
            self.chat()
        
        if command == "SAAT":
            self.time()