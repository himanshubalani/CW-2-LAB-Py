#Aim: Handle Multiple errors
def tidal():
	name = "Atharva"
	name += 5

def divide():
	try:
		tidal()
	except (NameError,TypeError ) as error:
		print(error)

divide()