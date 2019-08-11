s = input()
cntT = 0
cntC = 0
cntG = 0
for i in range(len(s)):
	if s[i] == 'T':
		cntT += 1
	if s[i] == 'C':
		cntC += 1
	if s[i] == 'G':
		cntG += 1
print(cntT * cntT + cntC * cntC + cntG * cntG + 7 * (min(min(cntC, cntG), cntT)))