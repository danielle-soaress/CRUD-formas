
from package.maths.Point import Point
from package.maths.Line import Line
from package.exceptions.Exceptions import InvalidAction

def workspace():
	try:
		print(f'\nEsse arquivo de teste foi feito para testar a entidade geométrica Reta')

		print(f'\nInsira os dados que serão pedidos. \n')
		print(f'Para que não haja erros, certifique-se que não tenha espeços desnecessários antes, depois e entre os dados. \n')

		name = input('Insira o nome da figura. Não há regras, pode conter apenas letras, apenas números, letras e números e caracteres especiais: ')

		print(f'\nAgora, insira as coordenadas de cada ponto no seguinte formato: "x y" \n Apenas números inteiros!!! \n')

		p1 = input('Ponto 1: ')
		p2 = input('Ponto 2: ')
		

		pointData = [p1.split(' '), p2.split(' ')]
		for i in range(len(pointData)):
			pointData[i] = list(map(int, pointData[i]))

		rect = Line(name, Point('p1',pointData[0][0],pointData[0][1]), Point('p2', pointData[1][0],pointData[1][1]), '#000')
		print(rect.model())

	except InvalidAction as e:
		print(e.message)
	except TypeError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados.')
	except ValueError as e:
		print('Erro! certifique-se que não tenha espeços desnecessários antes, depois e entre os dados.')
if (__name__ == "__main__"):
	workspace()
