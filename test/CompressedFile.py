from folder import directory


class CompressedFile:

	def __init__(self, file):
		self.filename = file
		self.dir = directory()

	def Compress(self):
		return None

	def Decompress(self, file):
		return None


# this is a simple byte read to dict algorithm, 
# only for myself, I don't know if it will make things smaller or not.
