from os import remove, spawnl

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
        if pro[0] == product['code'] or pro[1] == product['name']:
            return product
    return False


def add():
    print('Add/Edite new product whith below format')
    txt = input('code,name,price,count: ')
    new_product = txt.split(',')
    if check_exist(new_product) == False:
        f = open('database.csv', 'a')
        f.write('\n'+txt)
        f.close()
    else:
        print('duplicated production')
    load_data_from_file()

def edit(code):
    if search(code) == False:
        print("Product not found")
        return
    add()
    delete(code)


def delete(code):
    if search(code) == False:
        print("Product not found")
        return
    with open("database.csv", "r") as f:
        lines = f.read().split(',')
    with open("database.csv", "w") as f:
        for word in lines:
            if word != code:
                f.write(word + ',')

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
    product = search(code)
    if product == False:
        return False

    
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
                product['count'] = int(product['count']) - x
                f = open('database.csv', 'r')
                for row in f:
                    info = row[:-1].split(',')
                    if info[0] == code:
                        info[3] = product['count']
                        break
                with open("database.csv", "w") as f:

                        for word in info:
                            f.write(str(word) + ',')
                        
    

def save_and_exit():
    print('See you later')
    quit()


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
        code = int(input('Enter code of production: '))
        delete(code)
    elif choice == 4:
        show_list()
    elif choice == 5:
        var = input('Name or Code of product: ')
        if search(var) == False:
            print('Not found')
    elif choice == 6:
        code = input('Enter code of product: ')
        if buy(code) == False:
            print('Wrong product code or exit buying process')
    elif choice == 7:
        save_and_exit()    
