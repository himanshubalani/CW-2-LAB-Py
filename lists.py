#list functions
f = [1,2,3,4]       #basic lists
print(len(f))

list1 = list((12,2,3,48,76,8))     #using constructor
print(list1)

list1.insert(2,13)      #add element using insert - .insert(index,value)
print(list1)

list1.append(23)        #add element at the end using append - .append(value)
print(list1)

list1.remove(8)        #remove based on element in list - 
print(list1)

op = list1.pop()       #remove the last value
print(op)              #remove based on index of element
