print("Welcome to Roller Coster")
height = int(input("What is your Height in CM "))

bill = 0

if height >= 120:
    print("You can ride the Roller Coster ")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are Please pay $7.")
    else:
        bill = 12
        print("Adult tickets are Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry,You can't ride till you reach 120 cms ")
