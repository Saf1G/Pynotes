#Day 17 Simple inhertiance of objects time!
#Inhertiance means one class getting stuff from another class. The class that inherits is called child class and the class that he inherits "FROM" is called parent class
# A class can inherit from unlimited amount of other classes. And a class can also be inherited from multiply times

class Monster: # Monster class from before
	test_attribute = 50 # Here the test attribute is for simple inheritance
	 
	def __init__(self,health,energy): #Here to get this in the shark class if we have to call this in the child class
		self.health = health
		self.energy = energy

	def Attack1(self,damage):
		self.damage = damage
		return (f'{damage} damage has been dealt!')
	def Move(self,speed): #We don't want this in the shark class so how to overwrite it
		self.speed = speed
		return (f'The monster has moved at a speed of {speed}')

class Shark(Monster):  #For simple inheritance we have to add () after the class name and pass the class name which we want to inherit FROM
		#Attributes
	def __init__(self,speed,health,energy): #Here we have to add health,energy so we can add values to those
		self.speed = speed
		super().__init__(health,energy) #Here the super() calls the parent class then the __init__(health,energy) gets those attributes from the monster class
		#Method
	def Bite(self):
		return (f'The shark has bitten')
	def Move(self):  #Here we do this do overwrite the Monster class's Move function to overwrite both functions name MUST BE THE SAME
		return (f'The shark has moved at a speed of {self.speed}') # Using return statement is better than print because then we don't get 'none' after the output 

shark = Shark(speed = 60,health = 30,energy = 70)
print(shark.test_attribute) #The shark has inherited the monsters health which is 50
print(shark.Attack1(damage = 30)) #Here the monsters function also work perfectly fine
print(shark.Move())
print(shark.health) ; print(shark.energy) #Here this works we get both the health and energy values that we set for the shark and the attributes that the shark inherited

# Exercise (Passed)
#Create a scorpion class that inherits from the monster
#It should get health and energy from the parent
#it should have a poison_damage method
#Overwrite the Attack1 method to show poison damage

class Scorpion(Monster): #Step 1 inheriting
	def __init__(self,poison_damage,health,energy):
		self.poison_damage = poison_damage
		super().__init__(health,energy)
	def Attack1(self): #Poison damage attribute and overwriting the Attack1 to show poison damage
		return(f'The Scorpion has poisoned you and has dealt {self.poison_damage} poison damage!')

scorpion = Scorpion(poison_damage = 30,health = 100,energy = 40)
print(scorpion.Attack1()) # And the overwriting works


#   **Complex Inheritance**
# Child class inheriting from 2 parent class
#To do this we have to understand MRO = Method resolution order

class Monster1: # Monster class from before but this time this is Monster1
	def __init__(self,health,energy,**kwargs):  #Here we add keyword arguements unpacking
		self.health = health
		self.energy = energy
		super().__init__(**kwargs) 

		#Methods
	def Attack1(self,damage):
		self.damage = damage
		return (f'{damage} damage has been dealt!')

	def Move(self,speed):
		self.speed = speed
		return (f'The monster has moved at a speed of {speed}')

#Fish class for demonstration
class Fish:  
	def __init__(self,speed,has_scales):
		self.speed = speed
		self.has_scales = has_scales
	def swim(self):
		return(f'The fish is swimming at the speed of {self.speed}')

class Shark1(Monster1,Fish):

	def __init__(self,bite_strength,health,energy,speed,has_scales):
		self.bite_strenght = bite_strength
		super().__init__(health = health,energy = energy,speed = speed, has_scales = has_scales) #Here we follow the mro which is 
																					#[<class '__main__.Shark1'>, <class '__main__.Monster1'>, <class '__main__.Fish'>, <class 'object'>]
																					##First comes monster1 then fish so this super() is calling the monster1 class and inheriting from it

print(Shark1.mro()) #This is the order that we should call the functions at (output)
shark1 = Shark1(bite_strength = 40, health = 90, energy = 40,speed = 90,has_scales = True)
print(shark1.speed)
print(shark1.has_scales)



		




