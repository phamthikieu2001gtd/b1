
def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
a=int(input("nhap a: "))
total(a,1,2,3,5,6,Jack=11243,John=2231,Inge=1560)

