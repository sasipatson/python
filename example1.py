Data = {}
for n in range(5):
    name = input(f'Enter name %d : '%n)
    Data[n] = name

for n in Data:
    print(f'Data[%d] = %s'%(n,Data[n]))