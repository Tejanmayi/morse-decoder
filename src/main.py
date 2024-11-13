from driverFunctions import audio_to_morse, morse_to_audio



while(1):
    choice = input("1. Encrypt 2. Decrypt\n")
    
    if choice == "1":

        audio_to_morse()
    elif choice == "2":
        morse_to_audio()

    else:
        print("Try again")