#db username and pin
u_name=["name1","name2","name3"]
pin=["1","2","3"]

n=0
m=0
a=[None]*len(u_name)
b=[None]*len(pin)

#entering username and pin
for i in u_name:
    x=input("pls enter username ")
    a[n]=x
    n+=1

for j in pin:
    y=input("pls enter pin ")
    b[m]=y
    m+=1
    print("")

#verifying
if a==u_name:
    print("username correct")
else:
    print("username invalid")


if b==pin:
    print("pin accepted")
else:
    print("pin invalid")
    
    
if a==u_name and b==pin:
    print("please proceed")
elif a==u_name and b!=pin:
    print("reenter pin")
elif a!=u_name and b==pin:
    print("reenter username")
elif not(a==u_name and b==pin):
    print("reenter both")
