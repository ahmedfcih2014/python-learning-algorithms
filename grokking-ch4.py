def max(list):
    if len(list) == 2 :
        return list[0] if list[0] > list[1] else list[1]
    sub_list = list[1:]
    sub_max = max(sub_list)
    return list[0] if list[0] > sub_max else sub_max

l = [2,3,6,1,8,5,7]
print max(l)
