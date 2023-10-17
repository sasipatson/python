A = set()
Menu = ' 1. Add Item\n 2. Remove Item\n 3. Display Set\n 4. Exit'
while True:
    print(Menu)
    choice = int(input('Enter Choice : '))
    if choice == 1:
        print('Add Item')
        data = int(input('Enter number : '))
        A.add(data)
    elif choice == 2:
        print('Remove Item')
        data = int(input('Enter number to remove : '))
        A.remove(data)
        print()
    elif choice == 3:
        print(A)
    elif choice == 4:
        print('Exit Program')
        break
    else:
        print('No choice')
    