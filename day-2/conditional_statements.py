age=int(input("enter your age:"))
if(0<=age<=100):

 if age>=18:
    print("you are eligible for voter id and driving license")
 elif age<18:
    print("you are underage")   
else:
  print("invalid age enter your age between 0 and 100")        