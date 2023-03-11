print ("Student Information")




name = input("Enter your name: ")
roll = input("Enter your roll number: ")
reg = input("Enter your registration number: ")
mark = int(input("Enter your mark: "))

if mark >= 90:
    gpa = 4.0
elif mark >= 80:
    gpa = 3.5
elif mark >= 70:
    gpa = 3.0
elif mark >= 60:
    gpa = 2.5
elif mark >= 50:
    gpa = 2.0
elif mark >= 40:
    gpa = 1.5
else:
    gpa = 0.0

print("Name:", name)
print("Roll number:", roll)
print("Registration number:", reg)
print("Mark:", mark)
print("GPA:", gpa)

if mark >= 33:
    print("Pass")
else:
    print("Fail")
