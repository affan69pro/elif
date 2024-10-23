height=float(input("Enter your height in m:"))
weight=float(input("Enter your weight in kg:"))
BMI=height/weight**2
print("your BMI is=",BMI)
if BMI<=18.5:
    print("you are under weight")
elif BMI>=18.5 and BMI<=24.9:
    print("you are normal")
elif BMI>=24.9 and BMI<=29.9:
    print("you are over weight")
else:
    print("you are obese")