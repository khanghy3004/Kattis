n = int(input())
for _ in range(n):
	s = input().split()
	for i in range(len(s)):
		if(s[i] == "Simon" and s[i + 1] == "says"):
			for j in range(i + 2, len(s)):
				print(s[j], end = ' ')
			print('')