
from package.maths.Point import Point
from package.exceptions.Exceptions import *

def workspace():
	try:
		print(f'\nEsse arquivo de teste foi feito para testar a entidade geométrica ponto')

		print(f'\nInsira os dados que serão pedidos. \n')
		print(f'Para que não haja erros, certifique-se que não tenha espeços desnecessários antes, depois e entre os dados. \n')
		
		print(f'\nAgora, insira as coordenadas de cada ponto no seguinte formato: "x y" \n Apenas números inteiros!!! \n')
		
		p1 = input('Ponto 1: ')
		p2 = input('Ponto 2: ')
		
		pontos = [p1.split(' '),p2.split(' ')]
		
		for i in range(0,2):
			ponto = pontos[i]
			ponto = list(map(lambda x: int(x), ponto))
			pontos[i] = Point(f'p{i+1}',ponto[0], ponto[1] ,'#000')
			print(pontos[i].model())
	

		p1 = pontos[0]
		p2 = pontos[1]	
		print(f'\n Testando a relação entre os pontos: ')
		print(f'''
        Os pontos são diferentes? {'Sim' if p1.arePointsDifferent(p2) else 'Não'}
        Distância entre os pontos: {Point.distanceTo(p2):.2f}
        Mediana: {p1.medianBetween(p2)}
        ''')
		
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
