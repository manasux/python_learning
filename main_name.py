class Human:
	def __init__(self, name, age):
		self.name = 'Manas'
		self.age = 21 

	def do_work(self):
		if self.age == "21":
			print(self.name, "plays tennis")
		elif self.age == "27":
			print(self.name, "shoot a film")

	def speaks(self):
		print(self.name, "says how are you?")

tom = Human("manas", 27)
tom.do_work()
tom.speaks()

maria = Human("Maria sharapova")
