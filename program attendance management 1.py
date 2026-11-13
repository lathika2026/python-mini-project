students = {}
while True:
    print("1.register")
    print("2.attendance")
    print("3.display")
    print("4.percentage")
    print("5.exit")

    ch = int(input("enter choice:"))

    if ch == 1:
        roll = input("roll no:")
        name = input("name:")
        students[roll]=[name,[]]

    elif ch == 2:
        roll = input("roll no:")
        if roll in students:
            a=input("present or absent(P/A):")
            students[roll][1].append(a)

    elif ch == 3:
         for r in students:
             print(r,students[r])

    elif ch == 4:
         roll = input("roll no:")
         if roll in students:
             total=len(students[roll][1])
             present=students[roll][1].count("p")
             if total>0:
                 print("percentage:",present/ total*100)
    elif ch == 5:
         break
                      
