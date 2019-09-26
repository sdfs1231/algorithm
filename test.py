target=[]
with open('IntegerArray.txt','r') as f:
	target=f.readlines()
for x in range(len(target)):
	target[x]=int(target[x])
def f(A): 
	if len(A)==1:
		return 0
	else:
		rightStart=len(A)//2
		leftArray=A[0:rightStart]
		righArray=A[rightStart:]
		B,b=count_and_sort(leftArray)
		C,c=count_and_sort(righArray)
		D,d=count_and_sort_split(B,C)
		return b+c+d
def count_and_sort(A):
	if len(A)==1:
		return A,0
	elif len(A)==2:
		if A[0]<A[1]:
			return A,0
		else:
			temp=A[0]
			A[0]=A[1]
			A[1]=temp
			return A,1
	else:
		rightStart=len(A)//2
		leftArray=A[0:rightStart]
		righArray=A[rightStart:]
		B,b=count_and_sort(leftArray)
		C,c=count_and_sort(righArray)
		D,d=count_and_sort_split(B,C)
		return D,b+c+d
def count_and_sort_split(B,C):
	result=[]
	nums=0
	i=0
	j=0
	while i<len(B) or j<len(C):
		if i>=len(B):
			result=result+C[j:]
			break
		elif j>=len(C):
			result=result+B[i:]
			break
		if B[i]<C[j]:
			result.append(B[i])
			i+=1
		elif B[i]>C[j]:
			result.append(C[j])
			nums=nums+len(B[i:])
			j+=1
	return result,nums
print(f(target))