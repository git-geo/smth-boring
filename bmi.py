weight = float(input("Your weight: "))
height = float(input("Your height: "))

BMI = weight / height ** 2

if 18.5 <= BMI <= 25:
    print("Your weight is ok")
elif BMI < 18.5:
    print("You should gain weight")
else:
    print("You should lose weight")
