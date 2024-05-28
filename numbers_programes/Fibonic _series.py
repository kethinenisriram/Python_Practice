n=int(input("enter a number:"))
n1=0
n2=1
coun = 0

if n < 0 :
    Print("enter a valid number:")
elif n == 1:
    print("fibonicc series of 1 is 0")
else:
    while(coun < n):
        nextelement=n1 + n2
        print(nextelement)
        n1=n2
        n2=nextelement
        coun=coun + 1
