import math
import random
min_cut=float('inf')
# if 10<min_cut:
# 	min_cut=10
# print(min_cut)
# print(random.randint(1,201))
def read_data():
	data={}
	with open('kargerMinCut.txt','r+') as f:
		lines=f.readlines()
		for line in lines:
			line=line.strip().split('\t')
			line=map(int,line)
			line=list(line)
			data[line[0]]=line[1:]
	return data

def random_contract(data1):
	data=data1.copy()
	# if data==data1:
	# 	print('yes')
	vertices = list(data.keys())
	vertices_nums=len(vertices)
	temp=float('inf')
	while vertices_nums > 2:
		bnode=random.choice(vertices)

		# print('bnode is {}:{}'.format(bnode,data[bnode]))
		enode=random.choice(data[bnode])
		# print('enode is {}:{}'.format(enode,data[enode]))
		data[bnode]+=data[enode]
		for bonds in data[enode]:
			if bonds==bnode:
				data[bnode].remove(enode)
				data[bnode].remove(bnode)

			elif bonds!=bnode:
				# print(bonds)
				# print('bonds:{}:{}'.format(bonds, data[bonds]))
				data[bonds].remove(enode)
				data[bonds].append(bnode)
		# while bnode in data[bnode]:# inorder to remover circle
		# 	data[bnode].remove(bnode)
		del(data[enode])
		vertices = list(data.keys())
		vertices_nums = len(data.keys())
	# print(data)
	for v in data.keys():
		if len(data[v])<temp:
			temp=len(data[v])
			break
	return temp

for i in range(4000000):
	data=read_data()
	temp=random_contract(data)
	print('temp is %d'%temp)
	if temp<min_cut:
		min_cut=temp
	print('min_cuts is %d'%min_cut)


