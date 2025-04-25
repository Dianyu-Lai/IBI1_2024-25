"""
ask for input of weight and height
calculate the bmi
if bmi>30
print obese
if not >30 and <18.5
print too thin
else
print normal weight
"""
x=float(input("what's your weight (in kg)"))
y=float(input("what's your height (in m)"))
BMI = x/y**2
if BMI >30:
    print("you are obese")
elif BMI<18.5:
    print("you are too thin")
else:
    print("Congratulation! you have a normal weight")
