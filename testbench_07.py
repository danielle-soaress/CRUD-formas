from package.maths.Line import *
from package.maths.Point import Point

def workspace():
	print('Esse arquivo de teste foi feito para testar a Reta e o Segmento de Reta')
	l1 = Line('l1', Point('l1_p1', 2, 2), Point('l1_p2', 4, 7), '#000')
	l2 = Line('l2', Point('l2_p1', 7, 4), Point('l2_p2', 2, 8), '#000')
	s1 = LineSegment('s1', Point('s1_p1', 4, 2), Point('s1_p2', 14, 17), '#000')
	s2 = LineSegment('s2', Point('s2_p1', 2, 3), Point('s2_p2', 5, 8), '#000')

	print(l1.model())
	print(l2.model())
	print(s1.model())
	print(s2.model())

	print('Testing the relation between the lines.')

	print(
	f'''
	------- l1 and l2 ---------------
	Are Parallels? {'Yes' if l1.areParallels(l2) else 'No'}
	''')
	
	print(
	f'''
	------- s1 and s2 ---------------
	Are Parallels? {'Yes' if s1.areParallels(s2) else 'No'}
	Intersection: {s1.intersection(s2)}
	''')
	
	print(
	f'''
	------- l1 and s2 ---------------
	Are Parallels? {'Yes' if l1.areParallels(s2) else 'No'}
	''')
	
if (__name__ == "__main__"):
	workspace()
