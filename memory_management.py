from car import Car

def add_2(lst):
    lst += [4]
    print(lst, id(lst))

def update_immutable(num):
    print(f'before change {num}')
    num = 100
    print(f'after change {num}')

def update_mutable(lst):
    print(f'before change {lst}')
    lst = []
    print(f'after change {lst}')

def update_mutable_values(lst):
    print(f'before change {lst}')
    lst.append(5)
    print(f'after change {lst}')

if __name__ == "__main__":
    # lst1 = [1, 2, 3]
    # lst_cpy = lst1
    # lst2 = [4, 5, 6]
    # print(lst1, id(lst1))
    # print(lst_cpy, id(lst_cpy))
    # print(lst2, id(lst2))
    # lst1 += lst2
    # print(lst1, id(lst1))
    # print(lst_cpy, id(lst_cpy))
    #
    # car_1 = Car('toyota', 'corolla', 'red', 100)
    # car_2 = Car('toyota', 'corolla', 'red', 100)
    # print(id(car_1))
    # print(id(car_2))

    num = 50
    update_immutable(num)
    print(f'value of num after the function call: {num}')

    lst = [1,2,3,4]
    update_mutable_values(lst)
    print(f'value of lst after the function call: {lst}')