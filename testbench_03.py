from package.maths.Shapes import Triangle
from package.maths.Point import Point
from package.exceptions.Exceptions import *

def workspace():
	try:
		print(f'\nEsse arquivo de teste foi feito para testar a figura Triângulo')

		print(f'\nInsira os dados que serão pedidos. \n')
		print(f'Para que não haja erros, certifique-se que não tenha espeços desnecessários antes, depois e entre os dados. \n')


		name = input('Insira o nome da figura. Regras: no máximo 10 caracteres, pode conter apenas letras, apenas números, letras e números e caracteres especiais: ')

		print(f'\nAgora, insira as coordenadas de cada ponto no seguinte formato: "x y" \n Apenas números inteiros!!! \n')

		p1 = input('Insira o primeiro ponto da figura Triângulo: ')
		p2 = input('Insira o segundo ponto da figura Triângulo: ')
		p3 = input('Insira o terceiro ponto da figura Triângulo: ')

		pointData = [p1.split(' '), p2.split(' '), p3.split(' ')]
		for i in range(len(pointData)):
			pointData[i] = list(map(int, pointData[i]))

		triang = Triangle(name, Point('p1',pointData[0][0],pointData[0][1]), Point('p2', pointData[1][0],pointData[1][1]), Point('p3',pointData[2][0],pointData[2][1]), '#000')
		print(triang.model())

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
