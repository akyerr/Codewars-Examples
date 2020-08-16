"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

"""


# def tribonacci(signature, n):
#     if n == 1: 
#         return [signature[0]]
#     elif n == 0:
#         return []
#     elif n ==2:
#         return [signature[0],signature[1]]
#     else:
#     	for i in range(2, n-1):
#     		signature.append(signature[i]+signature[i-1]+signature[i-2])
#     	return signature


# print(tribonacci([1, 1, 1], 0))



def tribonacci(signature, n):
	if n <= 2:
		return signature[0: n]
	else:
		for i in range(2, n-1):
			signature.append(signature[i]+signature[i-1]+signature[i-2])
		return signature

print(tribonacci([1, 1, 1], 10))
