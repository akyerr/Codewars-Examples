"""you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer"""

def get_digits(n):
    new = []
    while n >= 10:
        new.append(n % 10)
        n = n // 10
    new.append(n)
    # print(new)
    return new[::-1]


x = get_digits(1234)
x = [n**2 for n in x]
result = ''
for i in x:
    result += str(i)

print(int(result))
