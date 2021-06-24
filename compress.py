def compress(string):
    length = len(string)
    result = ""
    count = 1
    for i in range(0, length):
        if i == length - 1:
            result += string[i]+str(count)
            break
        if string[i] != string[i+1]:
            result += string[i]+str(count)
            count = 1
        else:
            count += 1
    print(result)

compress("aabcccccaaa")

