# Script to test our encryption / decryption functions work.
#
# To see some of the background processes that are going on
# uncomment the visualizations I have added in previously,
# or add some more.

import random, sys, transpositionCipher, transpositionCipherDecrypt

def main():
	
	# number given is merely arbitrary starting point
	random.seed(43) 

	# run 20 tests
	for i in range(20):

		# return a string of a random quantity of the full alphabet
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
		
		# turn that string into a list
		message = list(message)
		
		# shuffles list
		random.shuffle(message)

		# convert list to string
		message = ''.join(message)

		# prints first 50 chars
		print('Test #%s: "%s..."' % (i+1, message[:50]))

		# for each letter of scrambled message
		for key in range(1, len(message)):

			# encrypts with key = (1-rand), message = alphabet
			encrypted = transpositionCipher.encryptMessage(key, message)

			decrypted = transpositionCipherDecrypt.transDecrypt(key, encrypted)

			# if output from decrypted is not same as origin show error
			if message != decrypted:

				print('Mismatch with key %s and message %s.' % (key, message))

				print(decrypted)

				sys.exit()

	print('Transposition cipher test passed.')

if __name__ == '__main__':
	main()
