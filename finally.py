def process_file():
	try:
		f = open("mk.txt")
		x = 1/0
	except FileNotFoundError as e:
		print("inside except")

	finally:
		print('cleaning up file')
		f.close()



process_file()