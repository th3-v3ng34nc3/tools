#python script to decode and encode morse code
#Author :  Aditya Raj aka th3-v3ng34nc3



from base64 import encode
from http.client import SWITCHING_PROTOCOLS


print("Input String to encode | Morse code to decode")
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
def encrypt(message1):
	cipher = ''
	for letter in message1:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '

	return cipher

def decrypt(message2):
	message2 += ' '

	decipher = ''
	citext = ''
	for letter in message2:
		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher
def main():
  message1 = input("Enter Message to Encode : ")
  result = encrypt(message1.upper())
  print (result)
  message2 = input("Enter Morse Code to decode : ")
  result = decrypt(message2)
  print (result)
if __name__ == '__main__':
	main()

