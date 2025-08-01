l=[]
e=[]
o=[]
n=int(input("Enter Number "))
for i in range(0,n):
	ele=int(input("Enter elements in list"))
	l.append(ele)
for i in range(0,n):
	if l[i]%2==0:
		e.append(l[i])
	else:
		o.append(l[i])
print(e)
print(o)
