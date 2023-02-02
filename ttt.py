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
	
	def place(self, pos, pl):
		self.state = self.state[:pos] + str(pl) + self.state[pos+1:]
		return self.state

	def end(self, state, pl):
		"""rows are 1, 2, 3; columns are 4, 5, 6; diagonal from 0 to 8 is 7; diagonal from 2 to 6 is 8"""
		checklist = set([i for i in range(1,9)])
		pl = str(pl)
		result = -1

		if self.state[0] != pl:
			checklist.discard(1)
			checklist.discard(4)
			checklist.discard(7)
		if self.state[2] != pl:
			checklist.discard(1)
			checklist.discard(6)
			checklist.discard(8)
		if self.state[6] != pl:
			checklist.discard(3)
			checklist.discard(4)
			checklist.discard(8)
		if self.state[8] != pl:
			checklist.discard(3)
			checklist.discard(6)
			checklist.discard(7)
		if self.state[4] != pl:
			checklist.discard(2)
			checklist.discard(5)
			checklist.discard(7)
			checklist.discard(8)

		for i in checklist:
			if i == 1:
				if self.state[0] == pl and self.state[1] == pl and self.state[2] == pl:
					result = 1
					break
			elif i == 2:
				if self.state[3] == pl and self.state[4] == pl and self.state[5] == pl:
					result = 2
					break
			elif i == 3:
				if self.state[6] == pl and self.state[7] == pl and self.state[8] == pl:
					result = 3
					break
			elif i == 4:
				if self.state[0] == pl and self.state[3] == pl and self.state[6] == pl:
					result = 4
					break
			elif i == 5:
				if self.state[1] == pl and self.state[4] == pl and self.state[7] == pl:
					result = 5
					break
			elif i == 6:
				if self.state[2] == pl and self.state[5] == pl and self.state[8] == pl:
					result = 6
					break
			elif i == 7:
				if self.state[0] == pl and self.state[4] == pl and self.state[8] == pl:
					result = 7
					break
			elif i == 8:
				if self.state[2] == pl and self.state[4] == pl and self.state[6] == pl:
					result = 8
					break
		return result

	def display(self, state=None):
		if state is None:
			state = self.state
		for j in range(3):
			for i in range(j*3, j*3 + 3):
				print(self.lookup[self.state[i]], end='  ')
			print()

	def Xsearch(self, state, d):
		if self.end(state, 1) or self.end(state, 2) or d == 0:
			return
		minLoss = 11
		for i in self.child(state, 1):
			ObestState = self.Osearch(i, d-1)
			if self.loss(ObestState, 1) < minLoss:
				minLoss = self.loss(ObestState, 1)
				XbestState = ObestState
		return XbestState

	def Osearch(self, state, d):
		if self.end(state, 1) or self.end(state, 2) or d == 0:
			return
		minLoss = 11
		for i in self.child(state, 2):
			XbestState = self.Xsearch(i, d-1)
			if self.loss(XbestState, 2) < minLoss:
				minLoss = self.loss(XbestState, 1)
				ObestState = XbestState
		return ObestState

	def loss(self, state, pl):
		op = 2 if pl == 1 else 1
		return self.lossFunction(state, pl) - self.lossFunction(state, op)

	def lossFunction(self, state, pl):
		op = '2' if pl == 1 else '1'
		pl = str(pl)
		checklist = set([i for i in range(1,9)])

		if self.state[0] == op:
			checklist.discard(1)
			checklist.discard(4)
			checklist.discard(7)
		if self.state[2] == op:
			checklist.discard(1)
			checklist.discard(6)
			checklist.discard(8)
		if self.state[6] == op:
			checklist.discard(3)
			checklist.discard(4)
			checklist.discard(8)
		if self.state[8] == op:
			checklist.discard(3)
			checklist.discard(6)
			checklist.discard(7)
		if self.state[4] == op:
			checklist.discard(2)
			checklist.discard(5)
			checklist.discard(7)
			checklist.discard(8)
		if self.state[1] == op:
			checklist.discard(1)
			checklist.discard(5)
		if self.state[3] == op:
			checklist.discard(2)
			checklist.discard(4)
		if self.state[5] == op:
			checklist.discard(2)
			checklist.discard(6)
		if self.state[7] == op:
			checklist.discard(3)
			checklist.discard(5)

		return len(checklist)

	def child(self, state, pl):
		temp = [x for x in range(len(state)) if state[x] == '0']
		l = []
		for i in temp:
			s = state[:i] + str(pl) + state[i+1:]
			l.append(s)
		return l
			