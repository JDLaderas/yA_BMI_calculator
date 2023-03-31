print("This is a BMI Calculator\n")

height = float(input("Please enter the height in m: "))
weight = float(input("Please enter the weight in kg: "))

calc = (weight / (height * height))

result = int("{:.0f}".format(calc))

print("your BMI is:",result)

if result <= 18.4:
    print(f"Your BMI is {result}, you are underweight.")
elif result <= 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result <= 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result <= 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")
