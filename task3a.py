def smallest(n:float , m:float) -> float:
    if n < m:
        return n #None of the provided calls because in both cases n < m was false
    else:
        return m

first = smallest(3, 2) #first = 2
second = smallest(2, 2) #second = 2 This is a reasonable result because 2 is not less than 2 so it returned 2
print(first)
print(second)