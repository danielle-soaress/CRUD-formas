from abc import ABC, abstractmethod

class Shape():

	def __init__(self, id, points, fillEnabled, fillColor = None):
		self.__id = id
		self.__points = points
		self.__fillEnabled = fillEnabled
		self.__fillColor = fillColor

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
	def draw(self):
		pass

	def remove(self):
		pass
	
	def leftMostPoint(self, points):
		LeftPoint = min(points, key=lambda ponto: ponto.getCoordX())
		return LeftPoint

	def rightMostPoint(self, points):
		RightPoint = max(points, key=lambda ponto: ponto.getCoordX())
		return RightPoint

	def lowestPoint(self, points):
		lowPoint = min(points, key=lambda ponto: ponto.getCoordY())
		return lowPoint

	def highestPoint(self, points):
		highPoint = max(points, key=lambda ponto: ponto.getCoordY())
		return highPoint
