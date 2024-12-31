#Day 5 slicing time woo
a_random_list = [1,2,3,'wordL',[2934,'random']]
print(a_random_list[1:6]) #this is indexing and here [start:end:step] is the direction and this is used to select certain items from a list 

default_slicing = a_random_list[::2]
print(default_slicing)

#slicing exercise 
#task = start from 8 and end at 2 and only pick every second element
excercise_list = [1,2,3,4,5,6,7,8,9,10]
print(excercise_list[7:0:-2])

#Unpacking
a,b = [6+9,5] #here the values 6+9 and 5 are assigned to a and b
print(a,b)
print(a)
print(b)

#exercise unpacking
value_1 = 10
value_2 = 'test'
#task switch the values
value_1,value_2 = value_2,value_1
print(value_1)
print(value_2)

#More strings,tuples and lists
#a string can be turned into a list using the split or the list function and a list/tuple can be turned into a string using the join function or the str function
turn_list = [1,2,3]
turn_string = 'happi happi happi'
print(str(turn_list))
print(''.join(turn_string))
#we can also index on strings like
print(turn_string[6])

#exercise
#task: remove brackets and commas from turn_list
result_variable = str(turn_list).strip('[').strip(']').replace(',','')
print(result_variable)