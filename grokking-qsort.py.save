def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i<= pivot]
    greater = [i for i in arr[1:] if i> pivot]
    return qsort(less) + [pivot] + qsort(greater)

test_list = [8 ,11 ,5 ,3 ,6 ,7 ,21]

print qsort(test_list)

