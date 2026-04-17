def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
 #the value of words at this point is ['this', 'is', 'confusing', 'code.', 'AVOID', "SUCH.']
 #the values of first and second are identical to the list above
 #the function surprising modified the list L in place using .append()
print(words)
print(first)
print(second)
