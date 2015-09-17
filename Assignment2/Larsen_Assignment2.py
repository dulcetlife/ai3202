#CSCI3202
#Assignment 3
#Henrik Larsen

import sys


class Node(object):
	def __init__(self, xval, yval, reachable):
		self.xval = xval
		self.yval = yval
		self.reachable = reachable
		self.parent = None
		self.distanceToStart = 0
		self.f = 0
		self.heuristic = 0

class Astar(object):
	def __init__(self):
		self.opened = []
		self.closed = set()
		#heapq.heapify(self.opened)
		self.nodes = []
		self.height = 8
		self.width = 10

	def get_heuristic(self,node,heur):
		#Manhattan distance
		if heur == '1':
			return 10*(abs(node.xval - self.end.xval) + abs(node.yval - self.end.yval))
		else:
			return 0

	def get_nodes(self, xval, yval):
		return self.nodes[xval*self.height + yval]
	def init_grid(self):
		grid, heuristic = inputandRead()

		for xval in range(self.width):
			for yval in range(self.height):
				if(xval,yval) in grid:
					reachable = False
				else:
					reachable = True
				self.nodes.append(Node(xval,yval,reachable))
		self.start = self.get_nodes(0,0)
		self.start = self.get_nodes(9,7)

		
						

def inputandRead():
	if len(sys.argv) !=3:
		print "Wrong number of arguments! Need to input a world and a heuristic function!"
		return (False,False)
	elif sys.argv[1] != "World1.txt" and sys.argv[1] != "World2.txt":
		print "Incorrect world! Pick between World1.txt and World2.txt!"
		return (False,False)
	elif sys.argv[2] != "Manhattan" and sys.argv[2] != "x":
		print "Wrong heuristic function! Pick between Manhattan and x!"
		return (False,False)
	else:
		m = open(sys.argv[1],'r')
		return(m,sys.argv[2])


def main():
	#world, heuristic = inputandRead()
	x = Astar()
	y = x.init_grid()
	print y


if __name__ == '__main__':
		main()	
