# more fun with global variables

def spam():
	global eggs
	eggs = 'spam'
	
eggs = 'global'
spam()
print(eggs)

input()