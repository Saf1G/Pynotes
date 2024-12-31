#Day 13 other comprehensions time! (complicated out of complicated)
#just like for lists we can use comprehensions for tuples dictionaries and sets some are similliar and some aren't

set_comprehension = {x for x in range(1,6)} #Set comprehension always starts with {} brackets and is just like lists
print(set_comprehension)

dict_comprehension = {x:x** 2 for x in range(1,6)} #Here this is a simple dictionary comprehension to get the sqr root of 25 16 9 4 and 1
#Here first we have a key which is x then we have a value which is x then we multiply the value with ** 2 then for x numbers in 1,6 we print 1 ** 2,2**2.....
print(dict_comprehension)

tuple_comprehension = (x for x in 'ABCD') #Here by using a tuple comprehension we print the word 'ABCD' in 4 rows 1 alphabet for each row
for x in tuple_comprehension:
	print(x)
#Here if we tried to print the tuple_comprehension we would get something like <generator object <genexpr> at 0x0000026D25744880> which is not helpful but we can use it in for loops
#A way to print this is to add the tuple function before the comprehension for example
#tuple_comprehension = tuple(x for x in 'ABCD')
#If we do that we will get ('A', 'B', 'C', 'D')

# exercise
#create a dictionary comprehension with the keys A B C D and E
#each key should have a list as value  with the values [1,2,3,4,5]

exercise_dict = {letter:[1,2,3,4,5] for letter in 'ABCDE'} #Here first we have the format key:value here letter:[1,2,3,4,5] then for each letter in the string 'ABCDE'
print(exercise_dict)                                       #The list is assigned to each alphabet 


#Sorting data
#Functions that take functions as arguements a good example of this is the 'sorted()' for functions where first you give a iterable then a function telling it how to sort it
sort_list1 = [1,3,5,7,42,9]
print(sorted(sort_list1)) #Here by giving it only 1 arguement it will sort a list from lowest number to highest numbers
#A way to sort it in reverse
print(sorted(sort_list1, reverse = True)) #Here by adding the reverse = True parameter we sort this list from high-low
#A way to sort a list which contains tuples and key value pairs
painful_list = [('a',3),('c',2),('b',10),('d',9),('g',13),('k',4)] 

def tuple_sorter(num):
	return num[0] #Here if we put the index 1 here it will look at the numbers and if we put the index 0 it will sort by string

print(sorted(painful_list,key = tuple_sorter)) # Here this is sorted by the alphabets a-z and the function should not be called rather should be just passed here
#An easier way to do this is to use a lambda function
print(sorted(painful_list,key = lambda number: number[1])) #Here this is sorted by the numbers low-high

# Exercise (Task 1 done,Task 2 failed)
#Sort this list by the mats availability (low-high)
#Sort this by the lenght of the material name
materials = ['Coal','Diamond','Gold','Iron','Netherite']  
mats_availability = [2,64,7,24,4]
mats_and_avail = list(zip(materials,mats_availability))
#Task 1
print(sorted(mats_and_avail,key = lambda num: num[1])) #Sorted by availability (low-high)
#Task 2
print(sorted(mats_and_avail,key = lambda alph: len(alph[0]))) #Sorted by the amount of alphabets in each material name (low-high)

#Map + Filter (Important

#It is like list comprehension and rarely used because it is replaced with list comprehension
#map =  it changes values with a function inside of an iterable
#filter = filters out values from a condition (very similliar to map)
def plus_5_func(num):
	return num + 5
my_list1 = [1,3,5,7,42,9]
print(list(map(plus_5_func,my_list1)))  #here we must convert it to a list first otherwise we will get values like <map object at 0x000001BAB12230A0>
     	  #Key        #Iterable

#a map function bascially goes through an iterable that makes a new list using the function we give as a key for example
#up there a +5 function is created where every number in the list got  +5'ed
#A lambda function can also be used instead of using an actual function
# Doing the plus_5_func with lambda functions
print(list(map(lambda x: x+5,my_list1))) #Here we add +5 to x and every value in the list is x so every value in the list is getting +5'ed

#Filters                                    #Note we also must convert this to a list/tuple/set etc etc otherwise we get values like <filter object at 0x000001BAB12230A0>
print(list(filter(lambda x: x>5,my_list1))) #Here we want to get the values which are more than 5 from the my_list1 so we create a lambda function for that
      			  #Key          #Iterable   #Instead of using a lambda function we can also use a normal function here like the plus_5_func

# Exercise (Task 1 done, Task 2 done)
#Create a list comprehension where every value in the my_list1 is +5'ed
#Create a list comprehension where values over 5 are only returned in the my_list1

plus_5_list = [x+5 for x in my_list1] #Task 1 +5'ed values in the my_list1 
print(plus_5_list)

#Only return values over 5
ret_more_5 = [x for x in my_list1 if x>5] #Task 2 only return values over 5 from the my_list1
print(ret_more_5)

