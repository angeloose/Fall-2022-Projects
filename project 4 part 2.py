file = open(r'projects\mobysmall.txt', 'a')
file.write("\nTesting,testing...")
file.close()
file = open(r'projects\mobysmall.txt')
name = str(file.read())
#name = '''
#If you've got time to fantasize about a beautiful death,
#why not live beautifully until the end?
#        '''


#A
print('(A)\n' + name)
print(name[::-1])

#B
z = input('(B)  Remove letter:')
name_no = ''
for character in name:
    if character != z:
        name_no += character
print(name_no)



#C and D
def char_num():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    letter_check = input('(C and D)  Find letter:')
    num_alpha = 0
    num_e = 0
    for character in name:
        if character in alphabet:
            num_alpha += 1
        if character == letter_check:
            num_e += 1
    e_percent = round((num_e/num_alpha)*100, 1)
    print("Your text contains", num_alpha, "alphabetic characters, of which", str(num_e), '(' +  str(e_percent) + '%)', "are", 'e' + ".")

#E and F
def no_e():
    character_check = input('(E and F)  Enter a character to check:')
    val = False
    for character in name:
        if character == character_check:
            val = True
    print(val)
    return val

#G
def no_e_modified():
    print('(G)  ')
    words = 0
    words_no_e = 0
    total_words_no_e = ''
    for word in name.split():
        words += 1
        if 'e' in word:
            words_no_e += 1
        else:
            total_words_no_e += word + ' '
    e_word_percent = round((words_no_e/words)*100, 1)
    print(total_words_no_e, '(' + str(e_word_percent) + ")% of words have no 'e'.")

#H
def avoids():
    wordie = input('(H)  Please enter a word:')
    forbidden_letters = input('Please enter forbidden letters:')
    x = True
    for character in wordie.lower():
        if character in forbidden_letters:
            x = False
    print(x)
    return x

#I
def uses_only():
    x = input('(I)  Please enter a word:')
    y = input('Please enter string of letters')
    check = True
    for character in x:
        if not character in y:
            check = False
    print(check)
    return check

#J 
def uses_all():
    x = input('(J)  Please enter a word:')
    y = input('Please enter string of letters')
    counter = 0
    letter_check = ''
    for character in x:
        if character in y:
            if character not in letter_check:
                letter_check += character
                counter += 1
    if len(y) == counter:
        print('True')
        return True
    else:
        print('False')
        return False

#K
def is_abecedarian():
    check = True
    x = input('(K)  Please enter a word:')
    x = x.lower()
    if not len(x) == 1:
        for i in range(1, len(x)):
            if x[i-1] > x[i]:
                check = False
                break
    print(check)
    return check

#L and M
def find():
    x = input('(L and M)  Find character:')
    y = int(input('Start at index:'))
    print(name.find(x,y))

#N
def is_sorted():
    x = input('(N)  Please enter a string of words:')
    x = x.lower().split()
    check = True
    for i in range(1, len(x)):
        if x[i-1] > x[i]:
            check = False
            break
    print(check)
    return check

#O
def is_anagram():
    x = input('(O)  Please enter first string:')
    y = input('Please enter second string:')
    if sorted(x.lower()) == sorted(y.lower()):
        print('True')
        return True
    else:
        print('False')
        return False

#P
def has_duplicates():
    x = input('(P)  Please enter a string:')
    check = False
    for character in x:
        if x.count(character) > 1:
            check = False
            break
        else:
            check = True
    print(check)
    return check

#Q
def remove_duplicates():
    x = input('(Q)  Please enter a string:')
    newx = ''
    for character in x:
        if x.count(character) <= 1:
            newx += character
        elif x.count(character) > 1 and not character in newx:
            newx += character
    print(newx)
    return


char_num() #C and D
no_e() #E and F
no_e_modified() #G
avoids() #H
uses_only() #I
uses_all() #J
is_abecedarian() #K
find() #L and M
is_sorted() #N
is_anagram() #O
has_duplicates() #P
remove_duplicates() #Q





    
