def main():
     # myMessage is 30 characters
     myMessage = 'Common sense is not so common.'
     myKey = 8

     ciphertext = encryptMessage(myKey, myMessage)

     # Shows end of output
     print('<output>' + ciphertext + '</output>')

def encryptMessage(key, message):

     # Each string in ciphertext represents a column in the grid.
     # ['', '', '', '', '', '', '', '']
     ciphertext = [''] * key
     
     # Range (0,8)
     for col in range(key):
     
         # pointer = 0, 1, 2, 3, 4, 5, 6, 7
         pointer = col
         
         # Keep looping until pointer goes past 30
         while pointer < len(message):
         
             # Add character at pointer to column
             ciphertext[col] += message[pointer]
             
             # visualize
             # print(ciphertext)

             # move pointer over
             pointer += key
             
             # visualize
             # print(pointer)

     # Join the ciphertext columns
     return ''.join(ciphertext)

# Starts script at given point
if __name__ == '__main__':
     main()
