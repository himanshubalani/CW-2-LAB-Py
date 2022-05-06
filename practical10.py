#Aim: parenthesis validation
class thor:
	def isvalid(str1):
		stack, paradict = [] , {"(" : ")","{":"}","[":"]"}
		for bracket in str1:
			if bracket in paradict:
				stack.append(bracket)
			elif len(stack) == 0 or paradict[stack.pop()] != bracket:
				return False
		return len(stack) == 0
	
print(thor.isvalid("{}[]()"))
print(thor.isvalid("()[{)}"))
print(thor.isvalid("()"))