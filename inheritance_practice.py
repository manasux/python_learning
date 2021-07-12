class Animal:
	def __init__(self, habitat):
		print(habitat, 'is a warm animal')


class Dog(Animal):
	def __init__(self):
		print("Dog has 4 legs")
		super().__init__('Dog')


d1 = Dog()