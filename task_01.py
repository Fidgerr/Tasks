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
        return True
    else:
        return False
