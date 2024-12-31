#Day 6 dictionaonaries time les gu
#dictionarie is a container like list and tuples
test_dict = {'random': 2123}
print(test_dict)
print(test_dict.values())

#Converting a dictionarie
print(list(test_dict))

#indexing on dictionaries
test_x2 = test_dict['random'] #can also use .get method for it but .get is better because
print(test_x2)
#print(test_dict['X']) will crash but
#print(test_dict.get['X']) won't crash but will return the value 'None'

#Exercise dictionaries
#task : use update method to add another key value to a dictionarie
exercise_dict = {'z': 12342,'2':'hello'}
print(exercise_dict)
exercise_dict.update({'AnotherValue' : 124})
print(exercise_dict)

#Sets 
#set is a datatype/container
test_set = {1,5,8,'Test',True,'ookla'} #sets cannot have a dupe value if it has a dupe value it will get deleted
turn_setTo_string = str(test_set).strip('{').strip('}').replace(',','')
print(turn_setTo_string) #btw indexing adn clicing do not work on sets

test_set2 = {1,2,True}
print(test_set - test_set2) #extra methods for sets are difference intersection the 'and' and |
print(test_set | test_set2) #etc etc

#exercise set
#detect dupes from a really long set
exercise_list = [1,2,4,5,6,7,2,4,6,7,1,4,134,646,8575,23,1,5356,757,25,868,2,64,88,1,856,4234,535,]
print(len(exercise_list))
print(len(set(exercise_list)))



