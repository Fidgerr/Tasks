def sort_list(list):
    min_el = 10000000
    min_counter = 0
    max_el = 0
    max_counter = 0
    if len(list) == 0:
        return list
    else:
        for i in range(len(list)):
            if min_el > list[i] > max_el:
                min_el = list[i]
                min_counter = i
                max_el = list[i]
                max_counter = i
            elif list[i] < min_el and list[i] < max_el:
                min_el = list[i]
                min_counter = i
            elif list[i] > min_el and list[i] > max_el:
                max_el = list[i]
                max_counter = i
            else:
                min_el = min_el
                max_el = max_el
        for i in range(len(list)):
            if list[i] == min_el:
                list[i] = max_el
            elif list[i] == max_el:
                list[i] = min_el
        list.append(min_el)
        return list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
