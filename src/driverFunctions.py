import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
from morsecode import encrypt, decrypt
from translate import translation_to_eng, translation_to_other, lang_options

ecount = 1


def SpeakText(command, opt):
     
    # Initialize the engine

    if opt == 1:
        message = list(command)
        command = ''
        for letter in message:
            if letter == '.':
                command += 'dot '
            if letter == '-':
                command += 'dash '
            if letter == ' ':
                command += 'space'
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    return command

def save_speech(command):
    global ecount
    speak = gTTS(text=command, slow=False)
    speak.save("encrypted_voice_" + str(ecount) +".mp3")
    print("Here is your file name: encrypted_voice_" + str(ecount) +".mp3")
    ecount += 1


def audio_to_morse():

    recognizer = sr.Recognizer()

    while(1):
        with sr.Microphone() as source:
            lang_options()
            src = input("\nWhich of these languages is your audio input?\n")
            # recognizer.adjust_for_ambient_noise(source)
            print("Listening..")
            audio = recognizer.listen(source)
            print("Got it, working on it!")

            try:
                # using google speech recognition
                text = recognizer.recognize_google(audio, language=src)

                

            except:
                print("Oops, I did not get that")

        ans = input("Did you say(Y/N): "+ text + "\n")
        if ans.lower() == 'y':
            en = encrypt(translation_to_eng(text).upper())
            print(en)
            morse_text = SpeakText(en, 1)
            

        save_choice = input("Would you like to save your encrypted speech? (Y/N)\n")
        if save_choice == 'y':
            save_speech(morse_text)
        break

def morse_to_audio():

    recognizer = sr.Recognizer()

    # morse code speech to English text

    while(1):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration= 1)
            print("Listening..")
            audio_text = recognizer.listen(source)
            print("Got it, working on it!")

            try:
                # using google speech recognition
                morse = recognizer.recognize_google(audio_text)

                res = input("Did you say(Y/N): "+ morse + "?\n")
                res = list(res)
                if 'y' in res:
                    decryption = decrypt(morse)
                    if decryption != False:
                        print("Your message: " + decryption)
                        de = SpeakText(decryption,0)
                        choice = input("Do you need translation?(Y/N)\n")
                        if choice.lower() == 'y':
                            translation_to_other(decryption)
                        break
                    
                    else:
                        raise Exception("Sorry, no morse code equivalent message for your text")
                

            except:
                print("Sorry, I did not get that")