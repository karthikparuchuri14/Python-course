marks=int(input("enter student marks:"))
if (0<=marks<=100) :
    if marks>=90:
        print("grade:A")
    if 90>marks>=80:
        print("grade:B")   
    if 80>marks>=70:
        print("grade:C")
    if 70>marks:
        print("grade:D")
else:
    print("invalid marks! please enter marks between 0 and 100")
                     