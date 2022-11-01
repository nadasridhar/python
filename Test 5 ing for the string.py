#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing'
#then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.


string = input('enter a name : ')
if len (string) >= 3:
    print ('your name : ', string + 'ing')

if string [-3:] == 'ing':
    print ('your name : ', string + 'ly')

else:
    len(string) < 3
    print ('your name : ', x)