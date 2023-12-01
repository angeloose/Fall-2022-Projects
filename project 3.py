import math
quarters = 25
dimes = 25
nickels = 25
ones = 0
fives = 0

price = 0
deposit = 0

def menu():
    print("\nMenu for deposits:\n'n' - deposit a nickel\n'd' - deposit a dime\n'q' - deposit a quarter\n'o' - deposit a one dollar bill")
    print("'f' - deposit a five dollar bill\n'c' - cancel the purchase")

def payment():
    global dollars
    global cents
    dollars = math.floor(rounded_price)
    cents = round(100*(math.fabs(rounded_price - dollars)))
    

def deposits(dp):
    global rounded_price, dep_nickel, dep_dime, dep_quarter, dep_dollar, dep_five, cancel_change, change_check
    if dp == 'n':
        rounded_price = (100*rounded_price - 5)/100
        change_check = (100*change_check + 5)/100
        dep_nickel += 1
    elif dp == 'd':
        rounded_price = (100*rounded_price - 10)/100
        change_check = (100*change_check + 10)/100
        dep_dime += 1
    elif dp == 'q':
        rounded_price = (100*rounded_price - 25)/100
        change_check = (100*change_check + 25)/100
        dep_quarter += 1
    elif dp == 'o':
        rounded_price = rounded_price - 1
        change_check = change_check + 1
        dep_dollar += 1
    elif dp == 'f':
        rounded_price = rounded_price - 5
        change_check = change_check + 5
        dep_five += 1
    elif dp == 'c':
        cancel_change = True
        rounded_price = 0 #breaks loop
    else:
        print('Illegal selection:', dp)
    change_check = round(change_check, 3)
    #print(change_check)    for testing purpose
    #print(rounded_price)
    #print(float(price))

def stock_purchase_change():
    global nickels, dimes, quarters, ones, fives 
    nickels += dep_nickel
    dimes += dep_dime
    quarters += dep_quarter
    ones += dep_dollar
    fives += dep_five

def stock_purchase_change_counter():
    global c_nickels, c_dimes, c_quarters, c_ones, c_fives 
    c_nickels += dep_nickel
    c_dimes += dep_dime
    c_quarters += dep_quarter
    c_ones += dep_dollar
    c_fives += dep_five

def stock_purchase_change_counter_part2():
    global nickels, dimes, quarters, ones, fives
    nickels += c_nickels
    dimes += c_dimes
    quarters += c_quarters
    ones += c_ones
    fives += c_fives

def purchase_change():
    global change, fives, ones, quarters, dimes, nickels, dep_nickel, dep_dime, dep_quarter, dep_dollar, dep_five 
    f = 0
    o = 0
    q = 0
    d = 0
    n = 0


    stock_purchase_change_counter()
            
    if change_check > round(float(price), 3):
        change = round(change_check - float(price), 3)
        dep_five = f
        change -= round(dep_five * 5, 3)    
        dep_dollar = o
        change -= round(dep_dollar * 1, 3)
        if quarters > 0:
            q = round((change*100)) // 25
            if quarters >= q:
                quarters -= q
            else:
                q = quarters
                quarters = 0
        dep_quarter = q
        change -= round((dep_quarter * 25)/100, 3)
        if dimes > 0:
            d = round((change*100)) // 10
            if dimes >= d:
                dimes -= d
            else:
                d = dimes
                dimes = 0
        dep_dime = d
        change -= round((dep_dime * 10)/100, 3)
        if nickels > 0:
            n = round((change*100)) // 5
            if nickels >= n:
                nickels -= n
            else:
                n = nickels
                nickels = 0
        dep_nickel = n
        change -= round((dep_nickel * 5)/100, 3)

        stock_purchase_change_counter_part2() #part 2 return deposited money
        c_nickels = 0
        c_dimes = 0
        c_quarters = 0
        c_ones = 0
        c_fives = 0
        
            
        change_display()
        
        if round(change, 3) > 0:
            print('Machine is out of change.\nSee store manager for remaining refund.')
            change_dollars = math.floor(change)
            change_cents = round(100*(math.fabs(change - change_dollars)))
            if change >= 1:
                print('Amount due is:', change_dollars, 'dollars and', change_cents, 'cents')
            else:
                print('Amount due is:', cents,'cents')
        
    else:
        print('No change due.')
        stock_purchase_change()
            
#def purchase_change_output():
    
    
def change_display():
    if dep_five > 0:
        print('', dep_five, 'five(s)')
    if dep_dollar > 0:
        print('', dep_dollar, 'dollar(s)')
    if dep_quarter > 0:
        print('', dep_quarter, 'quarter(s)')
    if dep_dime > 0:
        print('', dep_dime, 'dime(s)')
    if dep_nickel > 0:
        print('', dep_nickel, 'nickel(s)')

def total_stock():
    total = 0
    f = 0
    o = 0
    q = 0
    d = 0
    n = 0
    if fives > 0:
        total += 5 * fives
    if ones > 0:
        total += 1 * ones
    if quarters > 0:
        total += (25 * quarters)/100
    if dimes > 0:
        total += (10 * dimes)/100
    if nickels > 0:
        total += (5 * nickels)/100
    return total

    
        
    

print('Welcome to the vending machine change maker program\nChange maker initialized.')

while price != 'q':
    dep_nickel = 0       #reset deposited money
    dep_dime = 0
    dep_quarter = 0
    dep_dollar = 0
    dep_five = 0

    c_quarters = 0
    c_dimes = 0
    c_nickels = 0
    c_ones = 0
    c_fives = 0

    change = 0
    change_check = 0
    cancel_change = False
    
    print('\nStock contains:\n', nickels, 'nickels\n', dimes, 'dimes\n', quarters, 'quarters')
    print('', ones, 'ones\n', fives, 'fives\n')
    price = input("Enter the purchase price (xx.xx) or `q' to quit")
    if price == 'q':
            break
    rounded_price = round(float(price), 3)
    while rounded_price < 0 or round((rounded_price*100)) % 5 != 0:                           
        price = input("Illegal price: Must be a non-negative multiple of 5 cents.")
        if price == 'q':                                    #fix inputting q the second time
            break
        rounded_price = round(float(price), 3)
    menu()
    while (rounded_price >=1 and rounded_price > 0) or deposit != 'c':
        payment()
        print('Payment due:', dollars, 'dollar(s) and', cents, 'cents')
        deposit = input('Indicate your deposit:')
        deposits(deposit)
        if rounded_price < 1:
            break
    while rounded_price < 1 and round(rounded_price, 3) > 0:
        payment()
        print('Payment due:', cents,'cents')
        deposit = input('Indicate your deposit:')
        deposits(deposit)
    print('\nPlease take the change below.\n')
    if cancel_change == True:       #cancelled purchase refund
        change_check += float(price)
        purchase_change()
    else:
        purchase_change()
        

rounded_price = total_stock()
payment()
print('Total left in stock:', dollars, 'dollars and', cents, 'cents')


#test/fix bugs and do total amt
    
        
    
