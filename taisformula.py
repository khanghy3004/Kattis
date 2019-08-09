n = int(input())
area = 0
arr_t = []
arr_v = []
for i in range(0, n):
    t, v = map(float, input().split())
    arr_t.append(t)
    arr_v.append(v)
for i in range(0, n-1):
    area += (arr_t[i+1] - arr_t[i]) * (arr_v[i+1] + arr_v[i]) / 2000
print(area)