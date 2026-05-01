def smallest(n:float, m:float) -> float:
    if n < m:
        return n #both first and second are being evaluated in function smallest
    else:
        return m

first = smallest(3, 2) #the value of first is 2
second = smallest(2, 2) #the value of second is 2 and is reasonable because 2 is not less than 2
print (first)
print (second)