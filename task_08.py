def multiply_numbers(inputs=None):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if inputs is None:
        print('None')
    else:
        b = []
        a = list(str(inputs))
        for i in range(len(a)):
            if a[i] in numbers:
                b.append(a[i])
        if not b:
            b = 'None'
            print(b)
        else:
            pr = 1
            for i in range(len(b)):
                pr *= int(b[i])
            print(pr)


multiply_numbers()
multiply_numbers('ss')
multiply_numbers('1234')
multiply_numbers('sssdd34')
multiply_numbers(2.3)
multiply_numbers([5, 6, 4])
