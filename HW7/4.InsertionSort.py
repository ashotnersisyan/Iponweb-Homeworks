def insertion_sort(l):
    l_sorted = l.copy()
    length = len(l_sorted)
    for i in range(1, length):
        j = i
        while j > 0 and l_sorted[j-1] > l_sorted[j]:
            temp = l_sorted[j]
            l_sorted[j] = l_sorted[j-1]
            l_sorted[j-1] = temp
            j -= 1
    return l_sorted


print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([9, 8, 7, 6, 5]))
print(insertion_sort([7, 2, 9, 4, 5, 1]))
print(insertion_sort([6, 1, 9, 0, 2, 5]))
