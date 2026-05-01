def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) #the first call is being evaluated below this statement
    elif len(L) > 1: #the values being added are 4, 2, and 3 equaling to 9
        result = len(L[0]) + len(L[1]) #the third call is being evaluated below this statement
    elif len(L) > 0: #the values being added are 7 and 4 equaling to 11
        result = len(L[0]) #The second call is being evaluated below this statement
    else: #just the value 11
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print (first) #
print (second)
print (third)