from copy import *

arr = [1, 2, 4, 3, 5, 6]
n = len(arr)

arr_copy = arr.copy()
arr_copy.sort()
print(arr)
print(arr_copy)

if arr == arr_copy:
    print("yes")

l = r = -1

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        l = i
        break
for i in range(n - 1, 0, -1):
    if arr[i] < arr[i - 1]:
        r = i
        break

print(l, r)
temp = arr.copy()
temp[l], temp[r] = temp[r], temp[l]


if temp == arr_copy:
    print("yes")
    print("swap", l + 1, r + 1)

temp = arr.copy()


temp = temp[:l] + temp[r:l-1:-1] + temp[r+1:]
print(temp)

if temp == arr_copy:
    print("yes")
    print("reverse", l + 1, r + 1)
