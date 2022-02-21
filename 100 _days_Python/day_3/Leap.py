year = int(input("Which Year Do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("NOT LEAP YEAR. ")
    else:
        print("Leap Year. ")
else:
    print("Not Leap Year. ")
