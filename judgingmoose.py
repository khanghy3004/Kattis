l, r = input().split()
l = int(l)
r = int(r)
if l == 0 and r == 0:
	print("Not a moose")
elif l == r:
	print("Even", l + r)
else:
	print("Odd", max(l, r) * 2)