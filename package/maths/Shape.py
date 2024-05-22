from abc import ABC, abstractmethod

class Shape():

	def __init__(self, id, points, fillColor):
		self._id = id
		self._points = points
		self._fillColor = fillColor
		self.sortPoints()


	def getAPoint(self, i):
		return self._points[i]

	def setAPoint(self, i, value):
		self._points[i-1] = value
	
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

	@abstractmethod
	def model(self):
		pass
	
	def sortPoints(self):
		self._points = [
			self.highestPoint(self._points),
			self.lowestPoint(self._points),
			self.rightMostPoint(self._points),
			self.leftMostPoint(self._points)
		]

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
