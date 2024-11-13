import googletrans
from playsound import playsound
import pyttsx3
from gtts import gTTS 
from googletrans import Translator, constants
import os

def SpeakText(command, dest_lang):
     
    # Initialize the engine
    # engine = pyttsx3.init()
    # engine.say(command)
    # engine.runAndWait()
    speak = gTTS(text=command, lang=dest_lang, slow=False)
    speak.save("captured_voice.mp3")
  
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

translator = Translator()




def lang_options():
    print(googletrans.LANGUAGES)

def translation_to_eng(message):

    try:
        translation = translator.translate(message)
        eng_message = translation.text

    except:
        print("Oops, reloading..")
    # print(eng_message)

    return eng_message

def translation_to_other(message):
    lang_options()
    destination = input("\nPlease type the required target language:\n")
    # destination = find_dest(destination)
    translation = translator.translate(message, dest = destination)
    print(f"{translation.text} ({translation.dest})")
    SpeakText(translation.text, translation.dest)

