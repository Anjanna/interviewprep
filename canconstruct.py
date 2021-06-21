"""
Given a target word and an array of words
Return True if the word can be formed using the array of words,
False if not.
"""

def canconstruct(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in arr:
        if word == target[0:len(word)]:
            suffix = target[len(word):]
            if canconstruct(suffix, arr, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canconstruct("abcdef",["ab","abc","cd","def","abcd"])) #true
print(canconstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #false
print(canconstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
])) #false