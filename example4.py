from random import randint

def inputSales(Sales):
    for n in range(1,5):
        key = input('Enter branch name : ')
        value = []
        for m in range(1,5):
            data = float(input(f'Enter sales in Quarter {m} : '))
            value.append(data)
        Sales[key] = value

def calTotalSales(Sales):
    for key in Sales:
        total = 0.0
        for sale in Sales[key]:
            total += sale
        Sales[key].append(total)

def reportSales(Sales):
    print('='*76)
    print("| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |  Total  |")
    print('='*76)
    n = 1
    for key in Sales:
        print(f'| %2d  | %11s |'%(n,key),end='')
        for sale in Sales[key]:
            print(f'%8.2f|'%(sale),end='')
        print()
    print('='*76)

#main
Sales = {}
inputSales(Sales)
calTotalSales(Sales)
reportSales(Sales)
for key in Sales:
    print(key,Sales[key])
