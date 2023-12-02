def printary(ary):
    for i in range(len(ary)):
        print(ary[i], end=' ')


def rvsary(ary, start, end):
    while start < end:
        temp = ary[start]
        ary[start] = ary[end]
        ary[end] = temp
        start += 1
        end -= 1


def leftrotate(ary, sift):
    if sift == 0:
        return
    l = len(ary)
    rvsary(arr, 0, sift - 1)
    rvsary(arr, sift, l - 1)
    rvsary(arr, 0, l - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
d = 3
leftrotate(arr, d)
printary(arr)
