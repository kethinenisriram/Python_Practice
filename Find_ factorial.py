def fact(n):
    if n< 0 :
        print("it is not possiable for negitive no")
    elif n==0 or n==1:
        print(f"factoria of{n} is {1}")
    else:
       fac=1
       for i in range(2,n+1):
        fac=i*fac
    print(f"factorial of{n} is{fac}")

fact(6)





