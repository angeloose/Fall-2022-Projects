import math
code = input("Enter the customer's code:")
beg_meter = int(input("Enter the customer's beginning meter reading:")) 
end_meter = int(input("The customer's ending meter reading:" + "         "))

if (code == 'r' or code == 'R' or code == 'c' or code == 'C' or code == 'i' or code == 'I') and (-1 < beg_meter < 1_000_000_000 and -1 < end_meter < 1_000_000_000):
    print('Customer code:', code)
    if end_meter < beg_meter:
        gallons = (1_000_000_000 - math.fabs(end_meter - beg_meter))/10
    else:          
        gallons = (end_meter - beg_meter)/10

if code == 'r' or code == 'R':
    bill = 5 + (0.0005*gallons)
elif code == 'c' or code == 'C':
    if gallons < 4_000_001:
        bill = 1000
    else:
        bill = 1000 + (gallons-4_000_000)*0.00025
elif code == 'i' or code == 'I':
    if gallons < 4_000_001:
        bill = 1000
    elif 4_000_000 < gallons < 10_000_000:
        bill = 2000
    else:
        bill = 2000 + (gallons-10_000_000)*0.00025

else:
    print('Invalid Entry')
    gallons = 0
    bill = 0
print('Gallons of water used:', f'{gallons:0.1f}')
print('Amount billed: $' + f'{bill:0.2f}')



