from os import spawnl

PRODUCTS = []

def load_data_from_file():
    print('Loading...')

    f = open('database.csv', 'r')

    for row in f:
        info = row[:-1].split(',')
        new_dict = {'code':info[0], 'name':info[1], 'price':info[2], 'count':info[3]}
        PRODUCTS.append(new_dict)

    print('Database loaded. App is ready to use.')

def check_exist(pro):
    for product in PRODUCTS:
        if str(pro) == product['code'] or pro == product['name']:
            return product
    return False

def add():
    print('add new product whith below format')
    txt = input('code,name,price,count: ')
    new_product = txt.split(',')
    if check_exist(new_product) == False:
        f = open('database.csv', 'a')
        f.write('\n'+txt)
        f.close()
    else:
        print('duplicated production')
    load_data_from_file()

def edit():
    pass

def delete():
    pass

def show_list():
    print('code\tname\tprice\tcount')
    for product in PRODUCTS:
        print(product['code'], '\t', product['name'], '\t', product['price'], '\t', product['count'])

def search(var):
    for product in PRODUCTS:
        if product['name'] == str(var) or product['code'] == str(var):
            print('code\tname\tprice\tcount')
            print(product['code'], '\t', product['name'], '\t', product['price'], '\t', product['count'])
            return product
    return False

def buy(code):
    if check_exist(code) == False:
        return False

    product = search(code)
    while True:
        x = int(input('Enter number of count or 0 to exit: '))
        if x == 0:
            return False
        elif product['count'] < str(x):
            print("Not enough product")
        else:
            price = int(product['price']) * x
            print('Your cost ', price)
            cost = int(input('Enter number of cost: '))
            if price == cost:
                product['count'] = product['count'] - x
                f = open('database.csv', 'a')
                for row in f:
                    info = row[:-1].split(',')
                    if info[0] == code:
                        info[3] = product['count']
                        f.write()
                        f.close()
                    
                     
    

def save_and_exit():
    pass


def show_menu():
    print('Welcom to Sobhan store')
    print('1- Add')
    print('2- Edit')
    print('3- Delete')
    print('4- Show List')
    print('5- Search')
    print('6- Buy')
    print('7- Save and Exit')


load_data_from_file()
while True:
    show_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        add()
    elif choice == 2:
        code = int(input('Enter code of production: '))
        edit(code)
    elif choice == 3:
        delete()
    elif choice == 4:
        show_list()
    elif choice == 5:
        var = input('Name of product: ')
        if search(var) == False:
            print('Not found')
    elif choice == 6:
        code = input('Enter code of product: ')
        if buy(code) == False:
            print('Wrong product code or exit buying process')
    
