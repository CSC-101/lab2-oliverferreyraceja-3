def function2(a:int, b:int,c:int) -> int:
    if a > b and a > c:
        return a - b #a function will evaluate this statement first to determine a truth value
    elif b > c:
        return b + c #a function will evaluate this statement when the first statement was false
    else:
        return 2 * c #a function will evaluate this statement when the both the first and second statements were false

answer1 = function2(3, 2, 1)
answer2 = function2(2, 3, 1)
answer3 = function2(2, 1, 3)
print (answer1)
print (answer2)
print (answer3)