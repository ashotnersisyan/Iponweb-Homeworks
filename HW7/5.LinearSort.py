def linear_sort(l):
    l_sorted = []
    numbers_dict = {}
    l_min = float('inf')
    l_max = float('-inf')
    for elem in l:
        if elem > l_max:
            l_max = elem
        if elem < l_min:
            l_min = elem
        if elem in numbers_dict:
            numbers_dict[elem] += 1
        else:
            numbers_dict[elem] = 1
    for i in range(l_min, l_max+1):
        if i in numbers_dict:
            for _ in range(numbers_dict[i]):
                l_sorted.append(i)
    return l_sorted


print(linear_sort([1, 2, 3, 4, 5]))
print(linear_sort([9, 8, 7, 6, 5]))
print(linear_sort([7, 2, 9, 4, 5, 1]))
print(linear_sort([6, 1, 9, 0, 2, 5]))
