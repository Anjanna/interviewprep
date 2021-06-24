def checkpermute(stra, strb):
    dicta = {}
    for char in stra:
        if char not in dicta:
            dicta[char] = 1
    for char in strb:
        if char not in dicta:
            return False
    return True

print(checkpermute("anjanna", "jnaanna"))
print(checkpermute("abcde","fghij"))
print(checkpermute("abba", "baba"))
print(checkpermute("12345","678910"))