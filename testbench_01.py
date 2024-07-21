from package.maths.Shapes import Rectangle
from package.maths.Point import Point
from package.exceptions.Exceptions import *

def workspace():
	try:
		print(f'\nEsse arquivo de teste foi feito para testar a figura Retângulo')

		print(f'\nInsira os dados que serão pedidos. \n')
		print(f'Para que não haja erros, certifique-se que não tenha espeços desnecessários antes, depois e entre os dados. \n')


		name = input('Insira o nome da figura. Regras: no máximo 10 caracteres, pode conter apenas letras, apenas números, letras e números e caracteres especiais: ')

		print(f'\nAgora, insira as coordenadas de cada ponto no seguinte formato: "x y" \n Apenas números inteiros!!! \n')

		p1 = input('Insira o primeiro ponto da figura Retângulo: ')
		p2 = input('Insira o segundo ponto da figura Retângulo: ')
		p3 = input('Insira o terceiro ponto da figura Retângulo: ')
		p4 = input('Insira o quarto ponto da figura Retângulo: ')

		pointData = [p1.split(' '), p2.split(' '), p3.split(' '), p4.split(' ')]
		for i in range(len(pointData)):
			pointData[i] = list(map(int, pointData[i]))

		rect = Rectangle(name, Point('p1',pointData[0][0],pointData[0][1]), Point('p2', pointData[1][0],pointData[1][1]), Point('p3',pointData[2][0],pointData[2][1]), Point('p4', pointData[3][0],pointData[3][1]), '#000')
		print(rect.model())

	except InvalidAction as e:
		print(e.message)
	except InvalidName as e:
		print(e.message)
	except TypeError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados.')
	except ValueError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados.')
	except IndexError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados.')
if (__name__ == "__main__"):
	workspace()
