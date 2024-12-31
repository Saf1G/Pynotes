#Day 4 strings time
print('hello' + 'word')
 #strings is bascially the sentence we write between '' or "" we can also do some math operations with strings like 'hello' + 'random' 
print('hello'+'random')

test_variable_1 = "Quote of the day 'Ogaa is the best booga'"
print(test_variable_1) 
#escape chracter \ a_variable = '\'\"'
escape_character_variable = '\"\''
line_break_variable = 'Some text line 1 \n another random text \n again some more text'
print(escape_character_variable)
print(line_break_variable)
test_math_variable = 'Hello1' + 'World' + " " + 'Hello'
# How to get values into strings
Subject = 'Science'
Rating = 1200
Thing = 'operation'
print('I got a rating of {one} in my {two} {three}'.format(two = Subject,one = Rating,three = (Thing)))
#Method 2 of getting values in strings
String_value_Method2 = f'I got a rating of {Rating} in my {Subject} {Thing}'
print(String_value_Method2)

#String exercise
name =  'Saf'
hobby = 'Mogus films'
exercise_sentence = f'My name is {name}. \nMy hobby is {hobby}.'
print(exercise_sentence)

#Lists and tuples time
#lists and tuples are container which contain datatypes
list_test = [1,2,'Random Data'] ; tuple_test = (1,2,'random tuple data') #examples of lists and tuples (can also do "dir(variable_name))" for the methods of the list
#How to pick elements or values from a tuple or a list (the method of getting a value from a tuple or a list if called slicing)
print(list_test[2])
print(tuple_test[2])


#Excercise lists and tuples
#Task get the string "Hello :D"
exercise_list = ['first entry',[123,456,[0,'Hello :D']],'bye']
print(exercise_list[1][2][1])
