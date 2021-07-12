import json

book = {}
book['tom'] = {
	'name': 'tom', 
	'address': '1 res street, NY',
	'phone': 9918004063
}
book['bob'] = {
	'name': 'bob', 
	'address': '5 res street, NY',
	'phone': 6202286832
}


s = json.dumps(book) # converting dict to string
print(s)

with open('mk.txt', 'w') as f:
	f.write(s);	