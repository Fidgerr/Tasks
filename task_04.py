def sort_list(list):
    min_el = 10000000
    min_counter = 0
    max_el = 0
    max_counter = 0
    if len(list) == 0:
        print(list)
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
        list[min_counter] = max_el
        list[max_counter] = min_el
        list.append(min_el)
        print(list)


sort_list([])
sort_list([2, 4, 6, 8])
sort_list([1])
sort_list([1, 2, 1, 3])
