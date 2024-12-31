#day 2 methods returning values and comments
#method is just like functions but it is always attached to objects
Test_Method = 'A RANDOM TEST WORD'.lower()
print(Test_Method)
print(Test_Method.__len__())
print(Test_Method.upper())
some_name = 'Saf the G'
print(some_name.title())
print(some_name.strip('G'))
#print(dir(variable_name)) gives a list of methods that can be used

#excercise methods
excercise_string = 'I like beef'.replace('beef','mutton')
print(excercise_string)
#here the method replace is used to replace the word beef with mutton in the exercise_string variable

#returning values part 
#return is basically the value for example print(2+2) here 4 will be the value by using this we can combine mutiple values at once 
print(abs(len('a random test word word word yumm'.replace('word','cycle',))))
return_value_test = len('Very kewl word'.strip('d').replace('kewl','random'))
print(return_value_test)

#comments part 
#comments is basically this "#comments part" it does not interfere with the code but you can write anything in a comment and a comment starts with # and it can also be started with '''
comment_example = 'a variable to explain comments' #here the comment_example is the variable and 'a variable to explain comments' is a string
'''
here this is a comment 
'''
