print("This is the program to calculate the body mass index")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
BMI = float(weight) / (float(height) ** 2)
print("Your BMI is: ", BMI)
if BMI < 18.5:
    print("You are underweight")
elif 18.5 < BMI < 25:
    print("You have a normal weight")
elif 25 < BMI  < 30:
    print("You are slightly overweight")
elif 30 < BMI < 35:
    print("You are obese")
elif BMI > 35:
    print("You are clinically obese")