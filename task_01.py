def is_palindrome(string):
    string = str(string)
    string = string.lower()
    string = string.replace(' ', '')
    string = string.replace(',', '')
    string = string.replace('!', '')
    string = string.replace("'", '')
    string = string.replace("-", '')
    string = string.replace(".", '')
    string = string.replace("_", '')
    if string == string[::-1]:
        print('True')
    else:
        print('False')


is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")
