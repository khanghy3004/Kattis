sumN = 0
pen = []
correct = 0
for _ in range(30):
	pen.append(0)
while 1:
	a = input().split()
	if len(a) == 1:
		break
	if a[2] == "right":
		sumN += int(a[0]) + pen[ord(a[1])-65] * 20
		correct += 1
	else:
		pen[ord(a[1])-65] += 1
print(correct, sumN)
