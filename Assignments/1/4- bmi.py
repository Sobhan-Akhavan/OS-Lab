weight = float(input("Input weight: "))
height = float(input("Input height: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(bmi, "Underweight")
elif 18.5 <= bmi <= 24.9:
    print(bmi, "Normal")
elif 25 <= bmi <= 29.9:
    print(bmi, "Overweight")
elif 30 <= bmi <= 34.9:
    print("Obese")
elif 35 <= bmi:
    print(bmi, "Extermely Obese")
else:
    print("Your input wrong")