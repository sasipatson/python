A = {1,3,5,7,9}
B = {1,2,3,4,5}

Menu = ' 0. Display Set A,B\n 1. Union\n 2. Intersection\n'
Menu += ' 3. Difference\n 4. Symmetric_difference\n 5. Exit'

while True:
    print(Menu)
    choice = int(input('Enter choice : '))
    if choice == 0:
        print('Display Set A and Set B')
        print('Set A = ', A)
        print('Set B = ', B,'\n')
    elif choice == 1:
        print('Union Set')
        print('A union B : ',end='')
        print( A.union(B),'\n')
    elif choice == 2:
        print('Intersection Set')
        print('A intersection B : ',end='')
        print( A.intersection(B),'\n')
    elif choice == 3:
        print('Difference Set')
        print('A difference B : ', end='')
        print(A.difference(B),'\n')
    elif choice == 4:
        print('Symmetric_difference Set')
        print('A sysmmetric_difference B : ',end='')
        print(A.symmetric_difference(B),'\n')
    elif choice == 5:
        print('Exut Program')
        break
    else:
        print('No choice')