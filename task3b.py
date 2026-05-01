def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b #when a is stricly the largest value among the three
    elif b > c:
        return b + c #when a is not the largest, but b is strictly greater than c
    else: #
        return 2 * c #when a is not the largest and b is not greather than c

answer1 = function2(3, 2,1) #answer1 = 1
answer2 = function2(2, 3, 1) #answer2 = 4
answer3 = function2(2, 1, 3) #answer 3 = 6
print(answer1)
print(answer2)
print()
print(answer3)