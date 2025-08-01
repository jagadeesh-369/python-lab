l=[]
n=int(input("Enter number"))
for i in range(0,n):
	ele=int(input("Enter numbers in list"))
	l.append(ele)
	
print("max num is",max(l))
for i in range(0,n):
	if l[i]==max(l):
		index=i
print(index)

print("min num is",min(l))
for i in range(0,n):
	if l[i]==min(l):
		index=i
print(index)
