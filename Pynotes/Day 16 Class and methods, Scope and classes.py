#Day 16 Even more Class and methods time! (Important + 8 Hours into the video)
#Everything is an object in python and methods are basically functions  but they are a part of the object

def add(a,b): #
	return a+b

class Test1:
	def __init__(self,add_function):
		self.add_function = add_function

test1 = Test1(add_function = add)
print(test1.add_function(4,6))

#Exercise (Passed with some assistance)
#Create a Monster class with a parameter called func, store this func as a parameter (Task1)
#Create another class called Attacks that has 4 methods bite,strike,,slash,kick which just prints some random text (Task2)
#Create a monster object and give it one of the attack methods from the attack class (Task2)

class Monster: #Task 1 : Creating a Monster class with a parameter 'func'
	def __init__(self,func):
		self.func = func

class Attacks: #Task 2: Creating Attacks class with some attack methods
	def Bite(self):
		print('You have been bitten!')
	def Strike(self):
		print('The monster strikes!')
	def slash(self):
		print('The monster slashed you!')
	def kick(self):
		print('The monster kicked you L!')

attacks = Attacks() #Making the attacks class an object
Exercise_Monster = Monster(func = attacks.kick) #Task 3 : Passing a method from attack here as a method
Exercise_Monster.func()


#   **Classes and Scope!**

def health_update(amount):
	monster2.health += amount #Here this can update a local scope of a class

class Monster2:
	def __init__(self,health,energy):
		self.health = health 
		self.energy = energy

	def get_damage(self,amount): #For Exercise 2
		self.health -= amount 

monster2 = Monster2(70,30) #Turns Monster2 to an object

health_update(40) #Here the local scope health can be updated from a local scope
print(monster2.health)
print(monster2.energy)

# Exercise 2 (Failed)
#Create a hero class with 2 parameters damage and monster2 (which is the above monster2 object)
#The monster class should have a method that lowers their health -> get_damage(amount)
#The hero class should have an attack method that calls the get_damage method from the monster and the amount of damage is hero.damage

class Hero: #Step 1
	def __init__(self,damage,monster2):
		self.damage = damage
		self.monster2 = monster2

	def attack(self):
		self.monster2.get_damage(self.damage)

hero = Hero(50,monster2)
hero.attack()
print(monster2.health) #Monster health 110 - damage 50 = 60



