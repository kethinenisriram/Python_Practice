n=int(input("plaese enter a number :")) 
    
for i in range (2,n+1):
    for z in range(2,i):
        if i % z ==0:
            break
    else:
         print(i)  
