def smallest(n:float, m:float) -> float:
    if n < m:
        return n #the calls smallest(3,2) and smallest (2,2) are both being evaluated under this statement
    else:
        return m

first = smallest (3, 2) #the value of first is 2
second = smallest(2, 2) #the value of second is 2. This is reasonable result because in line 2, the if states only less than not a less than or equal to. Therefore, the execution skipped to line 5.
print (first)
print (second)

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b #a call will evaluate to this function when a is both greater than b and c
    elif b > c:
        return b + c #a call will evaluate to this function when b is greater than c while a is either not greater than b or c
    else:
        return 2 * c #a call will evaluate to this function if the statements above all result false

answer1 = function2(3, 2, 1) #the value of answer1 is 1
answer2 = function2(2, 3, 1) #the value of answer2 is 4
answer3 = function2(2, 1, 3) #the value of answer3 is 6
print (answer1)
print (answer2)
print (answer3)



