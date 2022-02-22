def greatest(num_list):
    indx = num_list[0]
    for i in num_list:
        if i > indx:
            indx = i
    return indx


num_list = [1, 23, 54, 86, 37]
great_num = greatest(num_list)
# great_num = greatest([1,23,54,86,37])
print("greater number in the list is ", great_num)
