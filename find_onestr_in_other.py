

# def scramble(s1, s2):
#     exist = []
#     for i in range(len(s2)):
#         if s2.count(s2[i]) <= s1.count(s2[i]):
#             exist.append(True)
#         else:
#             return False
#     return all(exist)


# print(scramble('scriptjavx', 'javascript'))


s1 = 'scriptjava'
print([char for char in s1])
s2 = 'javascript'
print([char for char in s2])

print([char for char in s2] in s1)
