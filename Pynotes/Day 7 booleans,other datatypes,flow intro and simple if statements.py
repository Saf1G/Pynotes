#Da7 (Very important) Boolean time!! 
#Boolean is basically a datatype which only has a value of true/false
boolean_test_variable1 = 'Boolean Test string'
print(boolean_test_variable1 == 'a random string') 
print(5 == 6) #is equals to ==
print(5 != 10) #is not equal to !=

#how to check if a value is in a container/datatype for example
print(2 in (5,'ookla string',6)) #operators to check the values are "in" and "not in"

#data conversion exercise (boolean)
#task : check if the key 1 and the value 'four' exists in the dictionarie
e_dict = {1:'one', 2: 'two', 3:'three'}
print('four' in e_dict.values()) #for 'four' 
print(1 in e_dict) #for the key 1
#also for extra
e_dict_updated = e_dict.update({4: 'four'}) #adds the key 4:'four' to the dictionary
print('four' in e_dict.values()) #checks for the value 'four' in the updated dictionary

#the bool() function
bool_func_test1 = 24924
print(bool(bool_func_test1))

#other datatypes time!
#just some datatypes which are not common but exist like none,sequence etc


#Flow intro time (important)
#Flow is bascially the order of the code for example if i have a simple if statement
statement_if_test = 5
if statement_if_test != 23:
	print('Then this will be printed and this belongs to the starting "if" function') #here the conditation and indentation is right so this is getting printed
#but if i printed it here then it would not belong to the if for example

#if bool_func_test1 == 123:  (also this is commented otherwise the code would be broken coz the indentation on print is not right take this as just an example)
print('Here the condition is false but still this is getting printed because the indentation or the flow of the code isnt right')


#Simple If statements (very much important)  
if statement_if_test == 5:    #here since the condition is met test if is getting printed instead of hi
	print('Test If')
else :
	print('Hi')

if statement_if_test != 5:    #here since the condition is NOT met Hi is getting printed instead of test if
	print('Test If')
else :
	print('Hi')
	

#simple if statements exercise yay
exercise_money = 100
#if money is greater or equal to 80 then eat fancy
#if money is greater than 45 eat something nice
#if money is greater than 15 eat something okay
#else eat something cheap
if exercise_money > 80:
	print('Eat fancy')
elif exercise_money > 45:
	print('Eat nice')
elif exercise_money > 15:
	print('Eat okay')
else :
	print('Eat cheap')








