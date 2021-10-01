x = float(input("Side x: "))
y = float(input("Side y: "))
z = float(input("Side z: "))

if x + y > z and x + z > y and y + z > x:
    print("Valid")
else:
    print("Invalid")