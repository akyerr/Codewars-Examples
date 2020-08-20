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
