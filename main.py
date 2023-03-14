print ("Student Information")




name = input("Enter your name: ")
roll = input("Enter your roll number: ")
reg = input("Enter your registration number: ")
mark = int(input("Enter your mark: "))



print("Name:", name)
print("Roll number:", roll)
print("Registration number:", reg)
print("Mark:", mark)

if mark >= 33:
    print("Pass")
else:
    print("Fail")
