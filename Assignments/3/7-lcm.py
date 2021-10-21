def lcm(a, b):
    if a == b:
        print('lcm = ',a)
    elif a < b:
        print('a < b')
    else:
        r = a / b
        t = b * int(r)
        if a == t:
            print('lcm = ', b)
        else:
            b2 = a - t
            a = b
            lcm(a, b2)

a=input('a = ')
b=input('b = ')
lcm(int(a),int(b))