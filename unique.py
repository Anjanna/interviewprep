def isunique(str):
    charmap = {}
    for char in str:
        if char in charmap:
            return False
        charmap[char] = 1
    return True

def uniqueMethod2(str):
    for i in range(1, len(str)-1):
        if str[i] == str[i-1]:
            return False
    return True

print(uniqueMethod2("abcde"))
print(uniqueMethod2("anjanna"))
print(uniqueMethod2("aaaabbbbb"))
print(uniqueMethod2("a1s2d3s6"))