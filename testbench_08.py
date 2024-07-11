from package.maths.CartesianPlane import *
from package.UI.UIManager import UIManager

def workspace():
	print(f'\nEsse arquivo de teste foi feito para testar o funcionamento da UI, no geral.')
	print(f'\nNo momento, a UI não está 100% desenvolvida e possui apenas uma função, feita exclusivamente para testar as ferramentas e a lógica necessária para criar a UI por completo.')
	print('Iniciando UI...')
	
	cartesianPlane = CartesianPlane()
	manager = UIManager(cartesianPlane)
	manager.run()

	
if (__name__ == "__main__"):
	workspace()
