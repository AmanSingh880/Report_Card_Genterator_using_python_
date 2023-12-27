print("""
================================================= WELCOME =================================================
""")
while(True):
    a=int(input("Enter 1 to exit or 2 to continue"))
    if(a==1):
        break
    else:
        name=input("Enter the name of Student : ")
        roll=int(input("Enter the Roll number of student : "))
        math=int(input("Enter the mark of Math : "))
        english=int(input("Enter the mark of English : "))
        hindi=int(input("Enter the mark of hindi : "))
        total=math+english+hindi
        filen=name+".txt"
        f=open(filen,"w")
        s=f"Roll No. = {roll}\nName = {name}\n------------------------------------------------------------------------------------------------------------\n"
        s+=f"\tMath\t = \t{math}\n"
        s+=f"\tEnglish\t = \t{english}\n"
        s+=f"\tHindi\t = \t{hindi}\n"
        s+="------------------------------------------------------------------------------------------------------------\n"
        s+=f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Total = {total}"
        f.write(s)
        f.close()
    
