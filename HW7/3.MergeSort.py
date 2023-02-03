def merge_sort(l):
    l_sorted = l.copy()
    if len(l_sorted) < 2:
        return l_sorted
    middle = (len(l_sorted)//2)
    left = l_sorted[:middle]
    right = l_sorted[middle:]
    merge_sort(left)
    merge_sort(right)
    n = 0
    m = 0
    k = 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            l_sorted[k] = l_sorted[n]
            n += 1
        else:
            l_sorted[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        l_sorted[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        l_sorted[k] = right[m]
        m += 1
        k += 1
    return l_sorted


print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([9, 8, 7, 6, 5]))
print(merge_sort([7, 2, 9, 4, 5, 1]))
print(merge_sort([6, 1, 9, 0, 2, 5]))
