a=float(input("Please Enter quantity to get bill:="))

if a<1000:
    print("No discount available!your bill is:",a*100,"Rs")
elif a>=1000:
    b=a*100
    c=10/100*b
    d=b-c
    print("congratulations you got 10% discount,you current bill is:",d,"Rs")
