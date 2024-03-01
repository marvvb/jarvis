import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/mb/new siri
eval "$(/opt/homebrew/bin/brew shellenv)"
api_key = "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"
lang = 'en'

openai.api_key = api_key

while True:
    def get_audio()
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Siri" in said
                   completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages =[{"role": "user", "content": said}])
                   text = completion.choices[0].message.content
                   speech = gTTs(text=text, lang=lang, slow=False, tld ="com.au")
                   speech.save("welcome1.mp3")
                   playsound.playsound("welcome1.mp3")

                   expect Exception:
                   print("Exception")

         return said

    get audio()


