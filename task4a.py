from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) #first value of test is False while the second value of test is True
    if test: #this check is preventing an index error to occur
        return L[idx]
    else: #
        return None

first = checked_access([1, 0, 1], 9) #the value of first is None
second = checked_access([1, 0, 1], 2) #the value of second is 1
print (first)
print (second)

