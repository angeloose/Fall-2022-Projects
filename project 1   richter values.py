print ('{:=^60}'.format('RESTART'))
print ('Richter{:^40}TNT'.format('Joules'))
print ('1{:^44}0.00047687913837688307'.format('1995262.3149688789'))
print ('5{:^42}476.87913837688404'.format('1995262314968.8828'))
print ('9.1{:^34}673609687.2046962'.format('2.818382931264449e+18'))
print ('9.2{:^34}951498973.5982201'.format('3.981071705534953e+18'))
print ('9.5{:^33}2681688466.3048882'.format('1.1220184543019653e+19'))

rval = float(input('Please enter a Richter scale:'))
energy = 10**((1.5 * rval) + 4.8)
#converted into joules
tnt = energy/(4.184*(10**9)) #converted into tons

print('Ricter scale value:', rval)
print('Equivalence in joules:', energy)
print('Equivalence in tons of TNT:', tnt)

