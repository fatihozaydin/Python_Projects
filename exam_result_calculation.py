exam1 = int(input("Point_1:"))
exam2 = int(input("Point_2:"))
final = int(input("Final_Point:"))


overall_grade =  exam1 * 3/10 + exam2 * 3/10 + final * 4/10

if (overall_grade >= 90):
    print("AA")
elif (overall_grade >= 85):
    print("BA")
elif (overall_grade >= 80):
    print("BB")
elif (overall_grade >= 75):
    print("CB")
elif (overall_grade >= 70):
    print("CC")
elif (overall_grade >= 65):
    print("DC")
elif (overall_grade >= 60):
    print("DD")
elif (overall_grade >= 55):
    print("FD")
else:
    print("FF")