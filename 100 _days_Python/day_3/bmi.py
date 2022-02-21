weight = int(input("What is your weight"))
height = int(input("What is your height"))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi},You are underweight. ")
elif bmi < 25:
    print(f"Your bmi is {bmi},You are normal weight. ")
elif bmi < 30:
    print(f"Your bmi is {bmi},You are Over weight. ")
elif bmi < 35:
    print(f"Your bmi is {bmi},You are Obese. ")
else:
    print(f"Your bmi is {bmi},You are Clinically Obese. ")
