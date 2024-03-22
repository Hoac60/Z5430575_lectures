def mk_csv_name(tic, show=True):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    name = f'{tic_base}_stk_prc.csv'
    if show is True:
        print(name)
    return name

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
        return evennum

is_even_num(list)

def squares_list():
    list1=[2, 3, 10, 14, 20, 21, 25, 13, 15]
    new_list=[]
    for i in list1:
        if i*i>150:
            new_list.append(i)
    print(new_list)
    return new_list
squares_list()

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result= [i for i in set (numbers) if i % 2 ==0]
result.sort()
print(result)

# Downloads Qantas share price beginning 1 January 2020
import yfinance                                     # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')       # (7)

def add(a,b):
    """ Returns the sum of two numbers """
    return a + b