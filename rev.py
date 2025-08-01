n=int(input("enter an number"))
rev=0
og=n
while n>0:
	temp=n%10
	rev=rev*10+temp
	n=n//10
print("The reverse number is",rev)	
if rev==og:
	print(rev,"is a palindrome")
else :
	print(rev,"is not a palindrome")
