message = 'Three can keep a secret, if two of them are dead.'

translated = ''

# length of the message is 49 | i is 48 as index starts at 0, not 1
i = len(message) - 1

# while i is greater than or equal to 0
while i >= 0:

	# first loop would return '.'
	# then '.d' and so on
	translated = translated + message[i]

	# print(i, message[i], translated)
	
	# next sequence
	i = i - 1

print(translated)
