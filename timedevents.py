import time

class vars:
	def __init__(self, seconds):
		self.initialTime = int(time.time())
		self.currentTime = int(time.time())
		self.seconds = seconds
		
		
	def determineTF(self): # Determine True of False to do an event
		self.currentTime = int(time.time())
		if self.initialTime + self.seconds <= self.currentTime:
				self.initialTime = int(time.time())
				return True
		else:
			return False
			
			
	def doFunction(self, function, *args):
		something = function(*args)
		self.initialTime = int(time.time())
		return something
