**## ai3202**

**## How to run the program:**
In the command line, type python Larsen_Assignment3.py <world> <heuristic>
You need to pick either World1.txt or World2.txt for the world, and Manhattan or Diagonal for the heuristic function.
Example: python Larsen_Assignment3.py World1.txt Manhattan - This will run through world1 using the manhattan function. 


**## My heuristic function:**
I picked the diagonal function as the second heuristic function. 
The equation for the diagonal function is:
x = abs(start.x - goal.x)
y = abs(start.y - goal.y)
return D*(x+y) + (D2 - D*2) * min(x,y)
D is the cost of moving up, down, right, or left.
D2 is the cost of moving diagonally. 

**## Performance:**

**### World1:**

**Manhattan:** The cost using the manhattan distance was 124, and it searched through 72 nodes.
**Diagonal:** The cost using the diagonal distance was 123, and it searched through 80 nodes.

**### World2:**
**Manhattan:**
**Diagonal**
