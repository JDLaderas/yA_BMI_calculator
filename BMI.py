print("This is a BMI Calculator\n")

weight = float(input("Please enter the weight "))
height = float(input("Please enter the height "))

calc = int(weight / (height * height))

print("your BMI is: ", calc)
