def compare(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

n = int(input())
line = []
for i in range(n):
    line.append(input())
if compare(line, sorted(line)):
    print("INCREASING")
elif compare(line, sorted(line, reverse=True)):
    print("DECREASING")
else:
    print("NEITHER")