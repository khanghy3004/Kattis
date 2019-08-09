a=[]
l = int(raw_input())
d = int(raw_input())
x = int(raw_input())
lenA = 0
def digits(number):
    assert number >= 0
    if number == 0:
        return [0]
    sumN = 0
    while number > 0:
        sumN += number % 10
        number = number // 10
    return sumN
for i in range(l,d+1):
    if digits(i) == x:
    	a.append(i)
    	lenA += 1
print a[0]
print a[lenA-1]
