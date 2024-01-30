def connect_dicts(dict1, dict2):
    sum1 = 0
    sum2 = 0
    for value in dict1.values():
        sum1 += value
    for value in dict2.values():
        sum2 += value
    my_dict = {}
    if sum1 > sum2:
        for key, value in dict1.items():
            if value >= 10:
                my_dict[key] = value
        for key, value in dict2.items():
            if value >= 10:
                if key not in my_dict:
                    my_dict[key] = value
    else:
        for key, value in dict2.items():
            if value >= 10:
                my_dict[key] = value
        for key, value in dict1.items():
            if value >= 10:
                if key not in my_dict:
                    my_dict[key] = value
    sorted_dict = dict(sorted(my_dict.items(), reverse=True))
    return sorted_dict
