alphabet = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
for i in range(n):
	phrase = input().lower()
	miss = ""
	for j in alphabet:
		if j not in phrase:
			miss += j
	if miss == "":
		print("pangram")
	else:
		print("missing", miss)