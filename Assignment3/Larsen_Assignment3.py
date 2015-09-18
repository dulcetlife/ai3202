#CSCI3202
#Assignment 3
#Henrik Larsen
#Got a lot of inspiration from this website:
# http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search
#Implemented in Python 3

import sys
import Queue



class Node(object):
	"""docstring for Node"""
	def __init__(self, xval, yval):
		self.xval = xval
		self.yval = yval
		distanceToStart = 0
		heuristic = 0
		f = 0
		parent = None
		
def makeGraph(world):
	graph = []
	world = open(world, 'r')
	for i in world.readlines():
		l = i.split()
		if(len(l)) > 0:
			graph.append([int(j) for j in l])
	return graph

def inputReader():
	if len(sys.argv) != 3:
		print "Need to provide world and heurstic function!"
		return(False, False)

	elif sys.argv[1] != "World1.txt" and sys.argv[1] != "World2.txt":
		print "Incorrect world provided!"
		return(False, False)
	elif sys.argv[2] != "Manhattan" and sys.argv[2] != "Diagonal":
		print "Incorrect heurstic function provided"
		return(False, False)
	else:
		m = sys.argv[1]
		return (m, sys.argv[2])


def manhattan(crd1, crd2):
	a = abs(crd1[0] + crd2[0])
	b = abs(crd1[1] + crd2[1])
	return 10*(a+b)

def diagonal(crd1, crd2):
	a = abs(crd1[0] + crd2[0])
	b = abs(crd1[1] + crd2[1])
	return 10*(a+b)+(14 - (2 * 10)) * min(a,b) 

def getStart(graph):
	start = (len(graph)-1, 0)
	return start

def getEnd(graph):
	end = (0, len(graph[0])-1)
	return end

def getLocation(coord,graph):
	x = coord[0]
	y = coord[1]
	return x,y

def getValid(coord, graph):
	x = coord[0]
	y = coord[1]
	x_end = len(graph) -1
	y_end = len(graph[x]) -1
	if x > 0 and y > 0 and y < y_end and x < x_end:
		return True
	else:
		return False

def checkWall(coord, graph):
	x = coord[0]
	y = coord[1]
	for i in range(-1,1):
		for j in range(-1,1):
			if graph[x+i][y+i] !=2:
				return True
				break
			else:
				return False
				break

def getAdjacent(coord, graph):
 
    y = coord[1]
    x = coord[0]
    x_end = len(graph)-1
    y_end = len(graph[x])-1

    cells= []
    if getValid(coord, graph) and checkWall(coord, graph):
        cells.append((x-1,y-1))

    if getValid(coord, graph) and checkWall(coord, graph):
        cells.append((x-1,y))

    if x > 0 and y < y_end and checkWall(coord, graph):
        cells.append((x-1,y+1))
   
    if getValid(coord, graph) and checkWall(coord, graph):
        cells.append((x,y-1))
    
    if getValid(coord, graph) and checkWall(coord, graph):
        cells.append((x+1,y-1))
    
    if getValid(coord, graph) and checkWall(coord, graph):
        cells.append((x+1,y))
    
    if getValid(coord,graph) and checkWall(coord, graph):
        cells.append((x+1,y+1))
    #For some weird reason, this one doesn't like getValid() and checkWall()
    if y < y_end and (graph[x][y+1] != 2):
        cells.append((x,y+1))
    return cells



def printPath(start, end, cells):
	history = []
	history.append(end)
	for i in range(0, len(cells)):
		if end != start:
			end = cells[end]
			history.append(end)
		else:
			break
	return history[::-1]


def checkCost(currentCell, nextCell, graph):
	if currentCell[0] == nextCell[0] or currentCell[1] == nextCell[1]:
		if graph[nextCell[0]][nextCell[1]] == 1:
			return 20
		else:
			return 10
	else:
		if graph[nextCell[0]][nextCell[1]] == 1:
			return 24
		else:
			return 14

def aStar(start, end, heuristic, graph):
	queue = Queue.PriorityQueue()
	queue.put((0, start))
	cost = {}
	cost[start] = 0
	cells = {}
	cells[start] = None
	bol = False
	while bol != True and queue.empty() != True:
		currentCell = queue.get()[1]
		if currentCell == end:
			bol = True
		if not bol:
			for next in getAdjacent(currentCell, graph):
				updateCost = cost[currentCell] + checkCost(currentCell, next, graph)
				if (next not in cost) or (updateCost < cost[next]):
					cost[next] = updateCost
					if heuristic == "Manhattan":
						important = updateCost + manhattan(currentCell, next)
						queue.put((important,next))
						cells[next] = currentCell
					else:
						important = updateCost + diagonal(currentCell, next)
						queue.put((important,next))
						cells[next] = currentCell
	return printPath(start,end, cells), cost[(end[0], end[1])], len(cost)
		
def main():
	world, heuristic = inputReader()
	manhattan = "Manhattan"
	diagonal = "Diagonal"
	graph = makeGraph(world)
	start = getStart(graph)
	end = getEnd(graph)
	if heuristic == manhattan:
		path, cost, nodes = aStar(start,end, manhattan, graph)
	else:
		path, cost, nodes = aStar(start, end, diagonal, graph)
	print "The path taken:", path
	print "The total cost for", world, "is:",cost, "with the", heuristic,"heuristic function"
	print nodes, "nodes were evaluted throughout the search"



	


if __name__ == '__main__':
		main()	
