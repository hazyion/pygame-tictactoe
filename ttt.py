class TTT:
	def __init__(self, state=None):
		self.state = state
		if state is None:
			self.state = '000000000'
		self.lookup = {
			'0' : '.',
			'1' : 'x',
			'2' : 'o'
		}
		self.endLookup = {
			1 : (0, 1, 2),
			2 : (3, 4, 5),
			3 : (6, 7, 8),
			4 : (0, 3, 6),
			5 : (1, 4, 7),
			6 : (2, 5, 8),
			7 : (0, 4, 8),
			8 : (2, 4, 6)
		}

		self.remLookup = {
			0 : (1, 4, 7),
			1 : (1, 5),
			2 : (1, 6, 8),
			3 : (2, 4),
			4 : (2, 5, 7, 8),
			5 : (2, 6),
			6 : (3, 4, 8),
			7 : (3, 5),
			8 : (3, 6, 7)
		}
	
	def place(self, pos, pl):
		self.state = self.state[:pos] + str(pl) + self.state[pos+1:]
		return self.state

	def end(self, pl, state=None):
		"""rows are 1, 2, 3; columns are 4, 5, 6; diagonal from 0 to 8 is 7; diagonal from 2 to 6 is 8"""
		if state is None:
			state = self.state
		checklist = set([i for i in range(1,9)])
		pl = str(pl)
		result = -1

		for i in checklist:
			end = True
			for j in self.endLookup[i]:
				if state[j] != pl:
					end = False
					break
			if end:
				result = i
				break

		return result

	def display(self, state=None):
		if state is None:
			state = self.state
		for j in range(3):
			for i in range(j*3, j*3 + 3):
				print(self.lookup[self.state[i]], end='  ')
			print()
		print()

	def Xsearch(self, state, d):
		if self.end(1, state) != -1 or self.end(2, state) != -1 or d == 0:
			return state
		XbestState = state
		minLoss = 9
		for i in self.child(state, 1):
			ObestState = self.Osearch(i, d-1)
			if self.loss(ObestState, 1) < minLoss:
				minLoss = self.loss(ObestState, 1)
				XbestState = i
		return XbestState

	def Osearch(self, state, d):
		if self.end(1, state) != -1 or self.end(2, state) != -1 or d == 0:
			return state
		ObestState = state
		minLoss = 9
		for i in self.child(state, 2):
			XbestState = self.Xsearch(i, d-1)
			if self.loss(XbestState, 2) < minLoss:
				minLoss = self.loss(XbestState, 2)
				ObestState = i
		return ObestState

	def loss(self, state, pl):
		op = 2 if pl == 1 else 1
		return self.gainFunction(state, op) - self.gainFunction(state, pl)

	def gainFunction(self, state, pl):
		op = 2 if pl == 1 else 1
		if self.end(pl, state) != -1:
			return 8
		if self.end(op, state) != -1:
			return 0

		pl = str(pl)
		op = str(op)
		checklist = set([i for i in range(1,9)])
		end = False

		for i in self.endLookup.keys():
			double = 0
			for j in self.endLookup[i]:
				if state[j] == pl:
					double += 1
				elif state[j] == op:
					break
			if double == 2:
				if end:
					return 7
				else:
					end = True
			
		for i in self.remLookup.keys():
			if state[i] == op:
				for j in self.remLookup[i]:
					checklist.discard(j)

		return len(checklist)

	def child(self, state, pl):
		temp = [x for x in range(len(state)) if state[x] == '0']
		l = []
		for i in temp:
			s = state[:i] + str(pl) + state[i+1:]
			l.append(s)
		return l

	def tie(self, state=None):
		if state is None:
			state = self.state
		for i in self.state:
			if i == '0':
				return False
		return True
			