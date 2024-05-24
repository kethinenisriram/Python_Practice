#sum of first ten numbers
def sum(n):
       x=1
       for i in range(0,n+1):
          x=x+i
       return x

z=sum(10)

print(f"sum of first 10 members is: {z}")