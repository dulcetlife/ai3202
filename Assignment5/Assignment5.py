#CSCI3202
#Assignment 5
#Henrik Larsen
#Implemented in Python3


import sys
import math

gamma = 0.9
s = 0.8
ns = 0.1



class MDP(object):
	"""docstring for MDP"""
	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.state = state
		self.delta = float("inf")
		self.utility = 0
		if state == 50:
			self.utility = 50
			self.reward = 50
			self.dir = "DONE"
		else:
			self.utility = 0
			self.dir = ""
			if state == 0:
				self.reward = 0
			elif state == 1:
				self.reward = -1 
			elif state == 2:
				self.reward = 0
				self.dir == "WALL"
			elif state == 3:
				self.reward = -2
			elif state ==4:
				self.reward = 1




	def possibleMoves():
		return


	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getState(self):
		return self.state
	def getReward(self):
		return self.reward
	def getPosition(self):
		return self.x,self.y
	def getDelta(self):
		return self.delta
	def getUtility(self):
		return self.utility
	def getDirection(self):
		return self.dir


	def setX(self,x):
		self.x = x
	def setY(self,y):
		self.y = y
	def setState(self,s):
		self.state = s
	def setReward(self,r):
		self.reward = r
	def setDelta(self,d):
		self.delta = d
	def setUtility(self,u):
		self.utility = u
	def setDirection(self,nd):
		self.dir = nd

	def __str__(self):
		return ("Current position: " + "(" + str(self.x)+ ", " + str(self.y) + "), Utility: " + str(self.utility))
def makeGraph(world):
	temp = open(world, 'r').readlines()
	newWorld = []
	for line in reversed(temp):
		newWorld.append(line.split())
	return newWorld[1:]

def CreateMap(mapp):
	newMapp = []
	for i in range(len(mapp)):
		newMapp.append([])
		for j in range(len(mapp[i])):
			newMapp[i].append(MDP(i,j,int(mapp[i][j])))
	return newMapp

def inputAndRead():
	if len(sys.argv) != 3:
		print "Need to provide world and a value for e!"
		return(False, False)
	elif sys.argv[1] != "World1.txt":
		print "Incorrect world provided! Need to be World1.txt"
		return(False, False)
	else:
		m = sys.argv[1]
		e = float(sys.argv[2])
		return (m, e)


def valueIteration(mapp,e):
	eq = 0.5*(1-gamma)/gamma
	delta = 10000
	while (delta > eq):
		delta = 0
		for i in range(7,-1,-1):
			for j in range(9,-1,-1):
				temp = utility(mapp,i,j)
				if temp > delta:
					delta = temp
	printPath(mapp)


def utility(mapp,i,j):
	node = mapp[i][j]	
	if(i + 1 >= 8):
		down = 0
	else:
		down = mapp[i+1][j].getUtility()
	if(i-1 <0):
		up = 0
	else:
		up = mapp[i-1][j].getUtility()
	if(j+1>= 10):
		right = 0
	else:
		right = mapp[i][j+1].getUtility()
	if(j-1<0):
		left = 0
	else:
		left = mapp[i][j-1].getUtility()

	probdown = s*down + ns*left + ns*right
	probup = s*up + ns*left + ns*right
	probright = s*right + ns*down + ns*up
	probleft = s*left + ns*down + ns*up


	optimal =[]
	optimal = optimalPath(mapp,i,j,probdown,probup,probright,probleft)
	t = optimal[0]
	old = node.getUtility()
	update = (node.getReward() + gamma*t)
	node.setUtility(update)
	node.setDirection(optimal[1])
	new = node.getUtility()
	return abs(new - old)
def printPath(mapp):
	x=0
	y=0
	cell = mapp[x][y]
	while cell.getDirection() != "DONE":
		print cell
		temp = str(cell.getDirection())
		t = str(cell.getPosition())
		if t == "(7, 9)":
			break
		if temp == "UP":
			x-=1
		elif temp == "DOWN":
			x+=1
		elif temp == "LEFT":
			x-=1
		elif temp == "RIGHT":
			y+=1
		cell = mapp[x][y]

def optimalPath(mapp,i,j,probdown,probup,probright,probleft):
	node = mapp[i][j]
	reward = node.getReward()
	optimal = max(probdown, probup, probleft, probright)
	if optimal == probdown:
		best = gamma*probdown + reward
		dirr = "DOWN" 
	if optimal == probup:
		best = gamma*probup + reward 
		dirr = "UP"
	if optimal == probleft:
		best = gamma*probleft + reward 
		dirr = "LEFT"
	if optimal == probright:
		best = gamma*probright + reward 
		dirr = "RIGHT"
	return (best,dirr)

def main():
	world, e = inputAndRead()
	world = makeGraph(world)
	mapp = CreateMap(world)
	valueIteration(mapp,e)

if __name__ == '__main__':
	main()

