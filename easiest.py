n = 1
def digits(number):
    assert number >= 0
    if number == 0:
        return [0]
    sumN = 0
    while number > 0:
        sumN += number % 10
        number = number // 10
    return sumN
while n != 0:
	n = int(raw_input())
	if n == 0:
		break
	for i in xrange(11,101):
		if(digits(n*i) == digits(n)):
			print i
			break