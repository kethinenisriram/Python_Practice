#Find the sum of all the multiples of 3 or 5 upto 10
n=int(input("please enter a number:"))
x=0
for i in range(1,n+1):
    if i%3 ==0 or i%5 ==0:
        x =i+x
print(x)