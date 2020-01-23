#program that prints the sum of the numbers in the string s.

string=input("enter the string")
string=string.split(',')
total=0
for i in string:
    total=total+float(i)

print("total: ",total)