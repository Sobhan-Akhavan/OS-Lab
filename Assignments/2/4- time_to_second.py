print("Please enter your time like: HH:mm:ss and 12H")
time = input("time: ")
split = time.split(':')
print("your time convert to second:",int(split[0]) * 3600 + int(split[1]) * 60 + int(split[2]))