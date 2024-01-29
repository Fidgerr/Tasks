def coincidence(list1=None, range1=None):
    if list1 is None:
        list1 = []
    a = []
    c = len(list1)
    for j in range(c):
        if type(list1[j]) == float and list1[j] // 1 in range1:
            a.append(list1[j])
        else:
            list1[j] = list1[j]
    d = len(list1)
    if list1 is not None and range1 is not None:
        for i in range(d):
            if list1[i] in range1:
                a.append(list1[i])
            else:
                a = a
        print(sorted(a), '\n')
    else:
        print(a, '\n')


coincidence([1, 2, 3, 4, 5], range(3, 6))
coincidence()
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
