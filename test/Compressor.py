import sys, os

class Compressor:
	"""Compress a file with a binary commression"""
	
	def __init__(self, path=os.path.abspath(__file__), filename=__file__, backdir=0):
		self.path = self.stripPath(path, backdir)
		self.fileName = os.path.basename(filename)
		self.binary = []
		self.fileData = []
		print(self.path)

	def getFileData(self):
		with open(self.path + self.fileName, 'rb') as file:
			for line in file.readlines():
				print(line)
				self.fileData.append(line)


	def stripPath(self, path, amountBack=0):
		pathsplit = path.split("\\")
		newPath = ""
		for pathElement in range((len(pathsplit)-1)-amountBack):
			newPath += pathsplit[pathElement] + "/"

		return newPath

	def CompressFile(self, filename=self.filename):
		pass