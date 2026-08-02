def second_smallest(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    mn, sec_mn = arr[0], arr[1]
    if sec_mn < mn:
        mn, sec_mn = sec_mn, mn

    for i in range(2, len(arr)):
        if arr[i] < sec_mn:
            sec_mn = arr[i]
        if arr[i] < mn:
            sec_mn = mn
            mn = arr[i]

    return sec_mn


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


print(second_smallest([5, -55, 3, 2, 10, 61]))
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(two_sum([2, 7, 11, 15, 3, 6], 9))
