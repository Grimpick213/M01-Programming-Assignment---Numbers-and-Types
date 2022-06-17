while(True):
    LastName = input("Enter your last name: ")
    if LastName == 'zzz':
        break
    FirstName = input("Enter your first name: ")

    GPA = float(input("Enter your GPA: "))
    if(GPA >= 3.5):
        print("Congratulations you made the Dean's List")
    elif(GPA >= 3.25):
        print("Congratulations you made the Honnor Roll")
