def replacespace(string, length):
    result = ""
    i = 0
    for char in string:
        if i > length-1:
            break
        if char.isspace():
            result += "%20"
        else:
            result += char
        i += 1
    print(result)

replacespace("Mr John Smith   ", 13)