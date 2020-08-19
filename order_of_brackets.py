"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
	if len(string) == 0 or (string.find('(') == -1 and string.find(')') == -1):
		return True 
	elif string.count('(') != string.count(')') or string[0] == ')' or string[-1] == '(':
		return False 
	count_o = 0
	count_c = 0
	for i in range(len(string)):
		if string[i] == '(':
			count_o += 1
		elif string[i] == ')':
			count_c += 1
		if count_c > count_o:
			return False
	return True 

"""
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
"""



