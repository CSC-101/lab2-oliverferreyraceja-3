from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) #the value of each test is a boolean that determines whether or not the index is within the valid range
    if test: #this check is preventing an index error
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9) #the value of first is None
second = checked_access([1, 0, 1], 2) #the value of second is 1
print(first)
print (second)

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) #it is evaluated for first.
    elif len(L) > 1: #the values added are 4, 2, and 3 ["this", "is", "the"]
        result = len(L[0]) + len(L[1]) #it is evaluated for third
    elif len(L) > 0: #the values added are 7 and 4 ["another", "call"]
        result = len(L[0]) #it is evaluated for second
    else: #the values added is just 11
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first)
print(second)
print(third)

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# the value of words is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#the value of both first and second is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#the function that returns L refrence the same original list, hence to why the answers of first and second are identical.
print(words)
print(first)
print(second)



