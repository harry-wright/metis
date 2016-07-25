message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# len(LETTERS) = 26
# range(len(LETTERS)) = (0,26)
# key = 0, 1, 2, 3, ... 25

for key in range(len(LETTERS)):
		# set translated to null after each loop
		translated = ''

		for symbol in message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol) # get the number of the symbol

				num = num - key

				if num < 0:
					num = num + len(LETTERS)

				# add number's symbol at the end of translated
				translated = translated + LETTERS[num]

			else:
				# just add the symbol without encrypting/decrypting
				translated = translated + symbol

		print('Key #%s: %s' % (key, translated))
