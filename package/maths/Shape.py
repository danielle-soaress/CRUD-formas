from abc import ABC, abstractmethod
from package.exceptions.Exceptions import InvalidShape

class Shape():

	def __init__(self, name, points, fillColor):
		self._name = name
		self._points = points
		self._fillColor = fillColor
		
		if not self.ArePointsDifferent():
			raise InvalidShape("A shape can't have identical points.")
		
		self.sortPoints()

# some getters and setters

	def getName(self):
		return self._name

	def getAPoint(self, i):
		return self._points[i]

	def getPoints(self):
		return self._points

	def getFillColor(self):
		return self._fillColor
	
	def setAPoint(self, i, value):
		self._points[i-1] = value
		
# abstract methods: (each class will develop it by itself)
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

	@abstractmethod
	def model(self):
		pass
	
# points methods: as each shape has many points (3 or more), each one must be responsible for deal with their set of point, 
# such as organizinge them, define how they will interact and the rules they must follow.
	
	def sortPoints(self):
		sorted_points = sorted(self._points, key=lambda p: (p.getCoordX(), p.getCoordY()))
		self._points = sorted_points
		
		points = []
		for p in sorted_points:
			points.append(p.getPoint())

	def ArePointsDifferent(self):
		points = []

		for p in self._points:
			points.append(p.getPoint())
	
		return True if len(set(points)) == len(self._points) else False

# string which contains all shape information

	def info(self):
		points_info = ''
		for point in self._points:
			points_info += f'{point.info()}, \n '


		return f'''Name: {self._name}

				Points:
				{points_info}

				Fill Color: {self._fillColor}
				'''