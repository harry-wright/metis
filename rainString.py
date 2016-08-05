# Found this:
# http://math.hws.edu/vaughn/cpsc/225/labs/vigenere.txt
# and wanted to loop it. Ctrl+C to abort.

import time

def main():

		# Length 95
		rainString = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

		rainFirst = rainString[0]
		
		charLimbo = ""
		
		while True:
		
			rainString = list(rainString)
		
			charLimbo = rainString[0]
		
			rainString.pop(0)
			
			rainString.append(charLimbo)
		
			rainString = ''.join(rainString)
			
			print(rainString)

			time.sleep(0.05)

if __name__ == "__main__":
	main()
