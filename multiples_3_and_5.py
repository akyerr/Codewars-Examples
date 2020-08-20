'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
'''


def solution(number):
    if number > 0:
        result = []
        for i in range(1, number):
            if i % 3 == 0 or i % 5 == 0:
                result.append(i)
            elif i % 3 == 0 and i % 5 == 0:
                pass
    return sum(result)


print(solution(0))
