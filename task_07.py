def combine_anagrams(words_array):
    dictionary = {}
    wrds = [''.join(sorted(list(x))) for x in words_array]
    for index, value in enumerate(wrds):
        if value in dictionary.keys():
            dictionary[value].append(index)
        else:
            dictionary[value] = [index]
    res = []
    for value in dictionary.values():
        a = []
        for index in value:
            a.append(words_array[index])
        res.append(a)
    return res
