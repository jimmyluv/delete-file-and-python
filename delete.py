import os
if  os.path.exists('text.txt'):

#try:
    os.remove ('text.txt')

#except FileNotFoundError as err:
    #print ('File Not Found')
else:
   print ('file not exists')

#os.remove ('abcd/text.txt')
#os.rmdir ('abcd')

                          