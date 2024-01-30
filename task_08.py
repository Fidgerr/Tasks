def multiply_numbers(inputs=None):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if inputs is None:
        return None
    else:
        b = []
        a = list(str(inputs))
        for i in range(len(a)):
            if a[i] in numbers:
                b.append(a[i])
        if not b:
            return None
        else:
            pr = 1
            for i in range(len(b)):
                pr *= int(b[i])
            return pr
