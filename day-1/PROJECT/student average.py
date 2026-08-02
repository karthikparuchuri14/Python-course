print("=== STUDENT AVERAGE CALCULATOR===")
name=input("ENTER YOUR NAME:")
print( "welcome to student average calculator",name)

sub1=float(input("enter marks of subject 1:"))
sub2=float(input("enter marks of subject 2:"))
sub3=float(input("enter marks of subject 3:"))

if (0<= sub1<= 100) and (0<=sub2<=100) and (0<=sub3<100):
       
      
    marks1=sub1
    marks2=sub2
    marks3=sub3
    total=sub1+sub2+sub3
    average=total/3
    print("TOTAL MARKS:",total)
    print("STUDENT'S AVERAGE:",average)
    if sub1>=35 and sub2 >=35 and sub3>=35:
        print("status:pass" )
    else:
        print("status:fail")

else:
    print("invalid marks! please enter marks between 0 to 100")


