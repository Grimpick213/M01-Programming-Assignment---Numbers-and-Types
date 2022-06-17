# Demitri Malher
# File Name : M02 Lab - Case Study
# The App asks the user to input their last name, first name and their GPA the program will then take their gpa and determine whether or not they made the honor roll the dean's list or neither

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
