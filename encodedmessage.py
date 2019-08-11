from math import sqrt

def printS(s):
	matrix = []
	k = 0
	lenS = int(sqrt(len(s)))
	for i in range(0, lenS):
		row = []
		for j in range(0, lenS):
			row.append(s[k])
			k += 1
		matrix.append(row)
	# for i in range(0, lenS):
	# 	print(" ".join(matrix[i]))
	for i in range(lenS-1, -1, -1):
		for j in range(0, lenS):
			print(matrix[j][i], end = '')
t = int(input())
for _ in range(t):
	s = input()
	printS(s)
	print("")
