dict1={"John":85,"Marshal":98,"Alice":45,"Rodrick":35}
key=str(input("NAME OF THE REGISTERED STUDENT : "))
if key in dict1:
    print(key,"STUDENT'S MARKS : ",dict1[key])
else:
    print("STUDENT NOT REGISTERED")

a=[1,2,3,4,5,6,7,8,9,10]
b=a[0:5]
print("THE ORIGINAL LIST IS : ",a)
print("EXTRACTED FIRST FIVE ELEMENTS : ",b)
b.reverse()
print("REVERSED EXTRACTED ELEMENTS : ",b)
