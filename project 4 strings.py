name = input("Please enter your name:")
listname = name.split()

#1. 
print('\nYour name is', len(name), 'characters long.')

#2.

print('\nThe last character is:', name[-1])

#3.

print('\nThe first ‘e’ is at position ' + str((name.find('e')) + 1) + '.')

#4.

num = 0
for word in listname:
    num += 1
print('\nYour name has', num, 'words.')

#5

print('\nYour first name is', listname[0])
#6.

vowels = ('a', 'e', 'i', 'o', 'u')
numvowels = 0
for character in name:
    if character in vowels:
        numvowels += 1
print('\nYour name contains', numvowels, 'vowels.')

#7.

uppername = ''
for character in name.lower():
    if character in vowels:
        uppername += character.upper()
    else:
        uppername += character
        
print('\nYour name with uppercase vowels is:', uppername)

#8.

print ('\n' + '{:+^70}'.format('{:~^50}'.format(name)))

#9. 

print ('\n' + '{:*<35}'.format(name[:len(name)//2]) + '{:*>35}'.format(name[len(name)//2:]))


