from package.maths.Shapes import Circle
from package.maths.Point import Point
from package.exceptions.Exceptions import *

def workspace():
	try:
		print(f'\nEsse arquivo de teste foi feito para testar a figura Círculo')

		print(f'\nInsira os dados que serão pedidos. \n')
		print(f'Para que não haja erros, certifique-se que não tenha espeços desnecessários antes, depois e entre os dados. \n')

		name = input('Insira o nome da figura. Regras: no máximo 10 caracteres, pode conter apenas letras, apenas números, letras e números e caracteres especiais: ')
		radius = input('Insira o raio do círculo. Apenas números inteiros. ')

		print(f'\nAgora, insira as coordenadas de cada ponto no seguinte formato: "x y" \n Apenas números inteiros!!! \n')

		p1 = input('Insira o ponto central da figura Círculo: ')

		p1 = p1.split(' ')

		circle = Circle(name, Point('p1', int(p1[0]), int(p1[1])), int(radius),'#000')
		print(circle.model())

	except InvalidAction as e:
		print(e.message)
	except InvalidName as e:
		print(e.message)
	except TypeError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados e se os dados cumprem os requisitos destacados.')
	except ValueError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados e se os dados cumprem os requisitos destacados.')
	
if (__name__ == "__main__"):
	workspace()
