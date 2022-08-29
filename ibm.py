weight = float(input("Your weight: "))
height = float(input("Your height: "))

ibm = weight / height ** 2

if 18.5 <= ibm <= 25:
    print("Your weight is ok")
elif ibm < 18.5:
    print("You should gain weight")
else:
    print("You should lose weight")
