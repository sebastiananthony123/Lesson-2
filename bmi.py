weight=float(input("enter a weight in kg: "))
height=float(input("enter a height in meters: "))

BMI = weight / (height * height)
print("your Body Mass Index(BMI) is", BMI)

if BMI<18.5:
    print ("you are underweight")

elif BMI >= 18.5 and BMI < 24.9 :
    print ("You are normal weight")

elif BMI > 25 and BMI < 29.9:
    print ("You are over weight")

elif BMI > 30 and BMI < 34.9:
    print ("you are obese!")
elif BMI > 35:
    print ("You are extremely obese")