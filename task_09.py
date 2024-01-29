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
    print(sorted_dict)


connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
