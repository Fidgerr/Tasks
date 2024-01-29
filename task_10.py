def count_words(string):
    string = string.lower()
    string = string.replace('  ', ' ')
    string = string.replace(',', '')
    string = string.replace('!', '')
    string = string.replace("'", '')
    string = string.replace("-", '')
    string = string.replace(".", '')
    a = list(string)
    words = []
    word = ''
    for i in range(len(a)):
        if a[i] != ' ':
            word += a[i]
            if i == len(a) - 1:
                words.append(word)
        elif a[i] == ' ' and a[i + 1] != ' ':
            words.append(word)
            word = ''
            continue
    my_dict = {}
    for i in range(len(words)):
        if words[i] not in my_dict:
            my_dict[words[i]] = string.count(f'{words[i]} ') + string.count(f' {words[i]}') - string.count(f' {words[i]} ')
    print(my_dict)


count_words("A man, a plan, a canal -- Panama")
count_words("Doo bee doo bee doo")
