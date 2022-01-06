import math  

num=int(input("Enter the number:"))

m=(num/10)%10

n=round(m)

l=len(str(num))

num = int((num // math.pow(10, l // 2))) % 10;

if l ==3 and num%3==0:

 print("Trendy Number")

else:

 print("Not a Trendy Number")
