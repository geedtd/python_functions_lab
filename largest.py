def largest(arr):
    largest = 0
    for num in arr:
        # print(len(arr))
        if num > largest:
            largest = num
    return largest

print(largest([1,2,3,4,5,88]))