s = input()
s += '0'
for i in range(len(s)-1):
	if s[i] != s[i+1]:
		print(s[i], end = '')