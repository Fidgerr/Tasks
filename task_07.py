def combine_anagrams(words_array):
    a = []
    for i in range(len(words_array)):
        words_array[i] = words_array[i].lower()
        if len(words_array[i]) not in a:
            a.append(len(words_array[i]))
    for i in range(len(words_array) - 1):
        if len(words_array[i]) > len(words_array[i + 1]):
            k = words_array[i]
            words_array[i] = words_array[i + 1]
            words_array[i + 1] = k
    a.sort()
    list1 = []
    for i in range(len(words_array[-1]) - len(words_array[0]) + 1):
        list1.append([])
    max_len = len(words_array[0])
    for i in range(len(list1)):
        for j in range(len(words_array)):
            if len(words_array[j]) == max_len:
                list1[i].append(words_array[j])
            else:
                if j == len(words_array) - 1:
                    max_len += 1
                else:
                    continue
    list2 = []
    for i in range(len(list1)):
        if list1[i]:
            list2.append(list1[i])
    for i in range(len(list2)):
        if len(list2[i]) == 1:
            list2[i] = list2[i]
        else:
            element = list2[i]
            letters = sorted(element[0])
            count = 0
            d = []
            for j in range(len(element)):
                if sorted(element[j]) == letters:
                    count += 1
                else:
                    d.append(element[j])
                    element[j] = ''
            if d:
                list2.append(d)
    for i in range(len(list2)):
        list3 = []
        element = list2[i]
        for j in range(len(element)):
            if element[j] != '':
                list3.append(element[j])
        list2[i] = list3

    print(words_array)
    print(list2)


combine_anagrams(["cars", "for", "potatoes", "racs", "four", "rouf", "scar", "creams", "arabic", "scream"])
