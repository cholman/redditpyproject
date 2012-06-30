import time

class vars:
	def __init__(self, seconds):
		self.initialTime = time.time()
		self.currentTime = time.time()
		self.seconds = seconds
		
		
	def determineTF(self): # Determine True of False to do an event
		self.currentTime = time.time()
		if self.initialTime + self.seconds <= self.currentTime:
				self.initialTime = time.time()
				return True
		else:
			return False
			
			
	def doFunction(self, function, *args):
		something = function(*args)
		self.initialTime = time.time()
		return something
