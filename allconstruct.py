"""
Given a target word and an array of words,
Return array of combinations from the input word array that 
can be used to generate the target word,
empty array if not.
"""

def allconstruct(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    result = []
    for word in arr:
        if word == target[0:len(word)]:
            suffix = target[len(word):]
            suffixWays = allconstruct(suffix, arr, memo)
            targetWays = [suffixWay+[word] for suffixWay in suffixWays]
            result = result + targetWays

    memo[target] = result
    return result

print(allconstruct("purple",["purp","p","ur","le","purpl"]))
print(allconstruct("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
print(allconstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(allconstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaz",[
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa"
]))