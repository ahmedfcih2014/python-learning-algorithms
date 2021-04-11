def b_search(list ,key ,iteration):
    if list == [] :
        return [-1 ,iteration]
    mid = len(list)/2
    if list[mid] == key:
        return [mid ,iteration]
    return b_search(list[mid:] ,key ,iteration + 1) if key > list[mid] else b_search(list[:mid] ,key ,iteration + 1)

l = [2 ,3 ,5 ,8 ,10 ,11 ,21 ,22 ,25 ,30 ,34 ,38 ,40 ,45]

test_1 = b_search(l ,11 ,1)

test_2 = b_search(l ,1 ,1)

if test_1[0] == -1:
    print 'test 1 show its not exists after:' ,test_1[1] ,'iteration'
else :
    print 'test 1 exists at:',test_1[0],'after:',test_1[1] ,'iteration'


if test_2[0] == -1:
    print 'test 2 show its not exists after:' ,test_2[1] ,'iteration'
else :
    print 'test 2 exists at:',test_2[0],'after:',test_2[1] ,'iteration'
