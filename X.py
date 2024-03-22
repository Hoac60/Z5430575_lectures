f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}

f_suburbs_pop = []
for key in f_suburbs:
    if key[0] != 'F':
        f_suburbs_pop.append(key)

for suburb in f_suburbs_pop：
    f_suburbs.pop(suburb)

f_suburbs.update({
    'Fairfield': 18081,
    'Fairfield East': 5273,
    'Fairfield Heights': 7517,
    'Fairfield West': 11575,
    'Fairlight': 5840,
    'Fiddletown': 233,
    'Five Dock': 9356,
    'Flemington': None,
    'Forest Glen': None,
    'Forest Lodge': 4583,
    'Forestville': 8329,
    'Freemans Reach': 1973,
    'Frenchs Forest': 13473,
    'Freshwater': 8866,
})
print (f_suburbs)


list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']

sol = list_a[1:7]

sol.remove('bad')

sol.append('including')

sol.insert(2, 'good')
sol.extend(list_b)
print(sol)


numbers = [-2,3,9,1,5,7,2,11,0,3,12,3,15,10]
print(max(numbers))

numbers = [-2,3,9,1,5,7,2,11,0,3,12,3,15,10]
largest_value = numbers[0]

for number in numbers:
    if number > largest_value:
        largest_value = number
        print(largest_value)





hours = input('enter the hours that you work')
hours = int(hours)
Normal_rate = 51.45
addtional_rate = 88.9

if hours > 35:
    pay = (35*Normal_rate)+((hours-35)*addtional_rate)
else:
    pay = hours *Normal_rate

print(f'this weekly payment is: {pay}')

import yfinance

start = '2020-01-01'

end = None

tickers = ["QAN.AX", "WES.AX"]

for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)

    tic_base = tic.lower().split('.')[0]

    df.to_csv(f'{tic_base}_stk_prc.csv')



numbers = [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]

L_number = numbers[0]
print ('before', L_number)

for number in numbers:
    if number > L_number:
        L_number = number
    print (f'The largest value is {L_number}')


def qan_tic():
    tic = "Qan.AX"
    print(tic)
    return tic

print(qan_tic())


def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)                # (6)
qan_tic()                 # (7)



def mk_csv_name (tic):
    tic=tic.lower()
    tic_base = tic.split('.')[0]
    return f'{tic_base}_stk_price.csv'

name = mk_csv_name('QAN.AX')
print (name)

evens = []
for x in range (1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)

print (evens [:10])


evens = [x for x in range (1_000_000 +1) if x % 2 == 0]
print(evens)



