from package.maths.User import User
from package.maths.Shapes import *
from package.maths.Point import Point

def workspace():
	user = User("Danielle", "dani", 312312, "danini@gmail.com", )
	print(user.profile())
	
	plane = user.getCartesianPlane()

	plane.UI.run()

if (__name__ == "__main__"):
	workspace()
