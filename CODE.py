dict1={"John":85,"Marshal":98,"Alice":45,"Rodrick":35}
key=str(input("NAME OF THE REGISTERED STUDENT : "))
if key in dict1:
    print(key,"STUDENT'S MARKS : ",dict1[key])
else:
    print("STUDENT NOT REGISTERED")
