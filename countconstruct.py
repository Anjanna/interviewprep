"""
Given a target word and an array of words
Return number of ways the word can be formed using the array of words,
0 if not.
"""

def countconstruct(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    number_of_ways = 0
    for word in arr:
        if word == target[0:len(word)]:
            suffix = target[len(word):]
            number_of_ways += countconstruct(suffix, arr, memo)
    memo[target] = number_of_ways
    return number_of_ways

print(countconstruct("purple",["purp","p","ur","le","purpl"])) #2
print(countconstruct("abcdef",["ab","abc","cd","def","abcd"])) #1
print(countconstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
print(countconstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
])) #0