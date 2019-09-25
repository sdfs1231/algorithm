def f(a):
	leftstart=0
	rightstart=(leftstart+len(a)-1)//2+1
	leftarray=a[leftstart:rightstart]
	rightarray=a[rightstart:]
	if len(leftarray)==1 or len(rightarray)==1:
		return merge(leftarray,rightarray)
	else:
		return merge(f(leftarray),f(rightarray))

def merge(leftarray,rightarray):
	temp=[]
	i=0
	j=0
	while i<len(leftarray) or j < len(rightarray):
		if i>=len(leftarray):
			temp=temp+rightarray[j:]
			break
		elif j>=len(rightarray):
			temp=temp+leftarray[i:]
			break

		if leftarray[i]<rightarray[j]:
			temp.append(leftarray[i])
			i+=1
		else:
			temp.append(rightarray[j])
			j+=1
		
	return temp

print(f([4,8,5,6,9,7]))