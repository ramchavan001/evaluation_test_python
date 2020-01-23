#Create a countdivisor(values in the variable(count), and variable(l,m,n) => should be assigned using map() function):
#Ex:
#Sample i/p:
#200 300 2
#O/p:	
#count = 50
#Then:
#Find the count of nos b/w 200 and 300 which will be divisible by 2(You should take other values while solving problem)


def count_divisor(list):
    count=0
    #return {c=c+1  for i in range(m,n+1) if i%l==0 }
    for i in range(m,n):
        if i%l==0:
            count=count+1
    return count 
    
    

m=int(input("enter the starting point: "))
n=int(input("enter the ending point: "))
l=int(input("enter the number for division "))

x=list(map(count_divisor, (l,m,n)))

print("count: ",x)


        
        
    