l=[]
n=int(input("Enter numbers in list"))
for i in range (0,n):
	ele=int(input("Enter an Element"))
	l.append(ele)
print(l)
print(sum(l))
print(sum(l)/len(l))
l.reverse()
print(l)
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)
