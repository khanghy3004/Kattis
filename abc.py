a = []
x, y, z = map(int, input().split())
a.append(x)
a.append(y)
a.append(z)
s = input()
a.sort()
for i in range(3):
	print(a[abs(ord(s[i]) - 65)],  end = " ")