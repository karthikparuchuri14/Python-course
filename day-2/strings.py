#string basic operations


# 1.concatenation
str1="ellenkicollege" 
str2="oftechnology"
finalstr=str1+str2


#lenght of string
print(finalstr)
print(len(finalstr))

#indexing
print(finalstr[4])


#slicing
print(finalstr[1:5]) #acessing parts of string
print(finalstr[0:len(finalstr)])
print(finalstr[0:26])
print(finalstr[0:])
print(finalstr[:26])


#negative slicing 
print(finalstr[-12:-5])
print(finalstr[-26:(len(finalstr))])


