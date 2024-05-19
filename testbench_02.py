from package.maths.terms import Circle

def workspace():
	data = input(f'Insira, separados por espaço, o raio e as coordenadas x e y no seguinte formato: x,y\n')
	radius, coordenates = data.split(" ")
	myCircle = Circle(radius, coordenates[0], coordenates[2])
	
	myCircle.print()
	
	
if (__name__ == "__main__"):
	workspace()
