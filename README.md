**## ai3202**

**## How to run the program:**
In the command line, type python Larsen_Assignment3.py <world> <heuristic>
You need to pick either World1.txt or World2.txt for the world, and Manhattan or Diagonal for the heuristic function.
Example: python Larsen_Assignment3.py World1.txt Manhattan - This will run through world1 using the manhattan function. 


**## My heuristic function:**
I picked the diagonal function as the second heuristic function.
I got the idea for this heuristic function from this website: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html 
The equation for the diagonal function is:
x = abs(start.x - goal.x)
y = abs(start.y - goal.y)
return D*(x+y) + (D2 - D*2) * min(x,y)
D is the cost of moving up, down, right, or left.
D2 is the cost of moving diagonally. 

I chose this heuristic function, because I thought it would find a faster and straigther way to the goal. Instead of going up and right, or down and left, it could now just go diagonally. So I picked this because I wanted a straigther path to the goal. However, my heurstic function had the same amount of cost as the Manhattan function, but it visited more nodes than the Manhattan function. This goes for both worlds. 

**## Performance:**

**### World1:**

**Manhattan:** The cost using the manhattan distance was 124, and it searched through 72 nodes.

	- Final Path: (7,0),(7,1),(6,2),(5,3),(5,4),(4,5),(3,5),(2,6),(1,7),(0,8),(0,9)
**Diagonal:** The cost using the diagonal distance was 123, and it searched through 80 nodes.

	- Final Path: (7,0),(7,1),(6,2),(5,3),(5,4),(4,5),(3,5),(2,6),(1,7),(0,8),(0,9)

**### World2:**

**Manhattan:** The cost using the manhattan distance was 146, and it searched through 69 nodes.

	- Final Path: (7,0),(7,1),(6,2),(6,3),(6,4),(5,4),(4,5),(3,5),(2,5),(1,6),(0,7),(0,8),(0,9)
    
**Diagonal:** The cost using the diagonal distance was 146, and it searched through 80 nodes.

	- Final Path: 7,0),(7,1),(6,2),(6,3),(6,4),(5,4),(4,5),(3,5),(2,5),(1,6),(0,7),(0,8),(0,9)
