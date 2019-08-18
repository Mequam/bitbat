#!/bin/python
def perm(n,r):
	ret_val = 1
	for i in range(0,r):
		ret_val *= (n - i)
	return ret_val

def fact(n):
	if n < 0:
		return -1
	if n == 1:
		return n
	else:
		return n*fact(n - 1)

def comb(n,r):
	return perm(n,r)/fact(r)
#c = int(input('(c)> '))
#r = int(input('(r)> '))

#print(comb(c,r))
#print(perm(c,r))
#print(fact(r))
BrdNum = 0
for i in range(1,9):
	BrdNum += perm(9,i)
arr = [(BrdNum,'BrdNum'),(3**9,'3^9'),(fact(9),'9!'),(BrdNum/fact(9),'BrdNum/9!')]

def key(val):
	return val[0]
arr.sort(key=key)

print('[',end='')
for val in arr:
	print(val[1],end=',')
print(']')

print('[',end='')
for val in arr:
	print(val[0],end=',')
print(']')

