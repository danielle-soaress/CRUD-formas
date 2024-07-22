from abc import abstractmethod
from package.maths.GeometricEntity import GeometricEntity
from package.exceptions.Exceptions import *

class Shape(GeometricEntity):

	def __init__(self, name, points, fillColor):
		try:
			super().__init__(name, fillColor)
			self._points = points
			
			if not self.ArePointsDifferent():
				raise InvalidAction("The points must be different.")
			
			self.sortPoints()
		except InvalidAction as e:
			raise
		except InvalidName as e:
			raise

# some getters and setters

	def getAPoint(self, i):
		return self._points[i]

	def getPoints(self):
		return self._points

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

	@abstractmethod
	def isPointInside(self):
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
	

