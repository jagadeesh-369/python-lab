n=int(input("Enter a number to check prime or not"))
count=0
for i in range(1,n+1):
	if n%i==0:
		count+=1
		
if count==2:
	print(n,"is a prime")
else:
	print(n,"is not a prime")		
		
