from package.maths.CartesianPlane import *
from package.UI.UIManager import UIManager

def workspace():
	print(f'\nEsse arquivo de teste foi feito para testar o funcionamento da UI, no geral.')
	print('Iniciando UI...')
	
	cartesianPlane = CartesianPlane()
	manager = UIManager(cartesianPlane)
	manager.run()

	
if (__name__ == "__main__"):
	workspace()
