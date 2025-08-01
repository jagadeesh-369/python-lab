i=0
j=1
fib=0
print("the fibonacci series is :")
print(i,j," ",end=" ")
while fib<500
	fib=i+j
	temp=fib
	fib=i
	print(fib," ",end=" ")
	i=j
	j=fib
