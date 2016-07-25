# usage
# python3.5 caesarCipher.py encrypt messagenospaces

from sys import argv
(script, usermode, usermsg) = argv

message = usermsg

# encrypt/decrypt key
key = 13

mode = usermode

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
	if symbol in LETTERS:
		# again a = 0, b = 1
		num = LETTERS.find(symbol)

		if mode == 'encrypt':
			num = num + key

		elif mode == 'decrypt':
			num = num - key

		# going past 'Z'
		if num >= len(LETTERS):
			# minus 26
			# So Z = 26, Z+13=39, 39-26=13, 13=M
			num = num - len(LETTERS)

		elif num < 0:
			num = num + len(LETTERS)

		translated = translated + LETTERS[num]

	else:
		# don't encrypt special chars
		translated = translated + symbol

print(translated)
