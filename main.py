from package.maths.CartesianPlane import *
from package.UI.UIManager import UIManager

def main():
	cartesianPlane = CartesianPlane()
	manager = UIManager(cartesianPlane)
	manager.run()

	
if (__name__ == "__main__"):
	main()
