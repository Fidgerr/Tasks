def max_odd(array):
    a = []
    count = 0
    maxx_odd = 0
    for i in range(len(array)):
        if type(array[i]) == int or type(array[i]) == bool or type(array[i]) == float:
            a.append(int(array[i]))
    for j in range(len(a)):
        if a[j] % 2 != 0 and a[j] > maxx_odd:
            maxx_odd = a[j]
            count += 1
    if count > 0:
        print(maxx_odd)
    else:
        print(None)


max_odd([1, 2, 3, 4, 4])
max_odd([21.0, 2, 3, 4, 4])
max_odd(['ololo', 2, 3, 4, [1, 2], None])
max_odd(['ololo', 'fufufu'])
max_odd([2, 2, 4])
