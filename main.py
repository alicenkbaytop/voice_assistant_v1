# import required modules

import speech_recognition as sr
import time
from command import Command

r = sr.Recognizer()

# asking cycle
while True:
    
    # getting sound
    with sr.Microphone() as source:
        print("Nasıl yardımcı olabilirim!")
        audio = r.listen(source)
        voice_data = ""
        
        # catching error
        try:
            voice_data = r.recognize_google(audio, language='tr-TR')
            print(voice_data)
            command = Command(voice_data)
            command.find_command()
            time.sleep(1)
            
        except sr.UnknownValueError:
            print("I didn't understand you!")
        except sr.RequestError:
            print("System is not working!")
            