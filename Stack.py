class Stack:


	def __init__(self):
		self._data = []

	def push(self, value):
		self._data.append(value)

	def pop(self):
		try:
			return self._data.pop()
		except:
			return None

	def peek(self):
		try:
			return self._data[self.size() - 1]
		except:
			return None

	def peekAt(self, i):
		try:
			return self._data[i]
		except:
			return None

	def size(self):
		return len(self._data)

	def copyFrom(self, aStack):
		self._data = []
		for i in range(0, aStack.size()):
			self._data.append(aStack.peekAt(i))
		pass

	def toString(self):
		string = ""
		for i in range(0, self.size()):
			string = string + str(self._data[i]) + "\n"
		return string