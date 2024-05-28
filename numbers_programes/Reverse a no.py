n=int(input("Please enter a number :"))
originalno=n

reverse=0

while n > 0:
    x=n % 10
    reverse = reverse * 10 + x
    n = n // 10

print(f"revere of {originalno} is {reverse} ")
