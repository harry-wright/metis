import math

def main():
	print("Transposition Decrypt")
	
	# len = 30
	message = "Cenoonommstmme oo snnio. s s c"
	
	key = 8
	
	output = transDecrypt(message, key)
	
	print(output + "|")
	
def transDecrypt(message, key):

	# round up 30/8 = 4
	numcols = math.ceil(len(message)/key)
	
	numrows = key
	
	array = [""] * numcols
	
	# number of boxes not used
	voidvals  = (numcols * numrows) - len(message)
	
	col = 0
	
	row = 0
	
	for symbol in message:
	
		array[col] += symbol
		
		# visualize
		#print (array)
		
		col += 1
	
		# resets when col value reached number of cols
		# or if we have reached a shaded box
		if (col >= numcols) or ( col == numcols - 1 and row >= key - voidvals ):
		
			col = 0
			
			row +=1
			
	result = ''.join(array)
	
	return (result)
	
if __name__ == '__main__':
	main()
