
# A dictionary is used to store the morse codes for each letter in the English alphabet and the special characters
MORSE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}


#function to convert morse text in (dot dash) into (. _) format

def convert(message):
    lst = list(message)
    morsecode = ""
    for word in lst:
        word = word.lower()
        if word == "dot" or word ==".":
            morsecode += '.'
        if word == "dash" or word == "-":
            morsecode += '-'
        if word == "space":
            morsecode += ' '
    
    return morsecode

# encrypt function encrypts the text message into morse code using the morse code dictionary
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += MORSE_DICT[letter] + ' '
		else:
			cipher += ' '

	return cipher

# decrypt function decrypts the morse code into text using the morse code dictionary

def decrypt(message):


    message = convert(message)
    message += ' '

    decipher = ''
    citext = ''

    try:
        for letter in message:

            # checking for space between the characters
            if (letter != ' '):

                # a counter to keep track of spaces
                i = 0

                citext += letter

            
            else:
                # if space is one then it indicates a new character
                i += 1

                # if space is 2 then it indicates a new word
                if i == 2 :

                    # appending space to distinguish words
                    decipher += ' '
                else:
                    
                    decipher += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(citext)]
                    citext = ''

    except:
        return False


    return decipher