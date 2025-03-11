"""
BEGIN
    DISPLAY "What's your weight (in kg)?"
    INPUT x  // Read user's weight in kg

    DISPLAY "What's your height (in m)?"
    INPUT y  // Read user's height in meters

    COMPUTE BMI = x / (y * y)  // Calculate BMI

    IF BMI > 30 THEN
        DISPLAY "You are obese"
    ELSE IF BMI < 18.5 THEN
        DISPLAY "You are too thin"
    ELSE
        DISPLAY "Congratulations! You have a normal weight"
    END IF
END
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