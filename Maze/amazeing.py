#maze generation using depth first algorithm
#https://en.wikipedia.org/wiki/Maze_generation
import Image, ImageDraw
import random

cellstack = []
img = Image.new("RGB", (10, 10), "white")
draw = ImageDraw.Draw(img)
#create cell Class with necessary variables
class Cell(object):
      def __init__(self, visited, current, cx, cy):
          self.visited = visited
          self.current = current
          self.x = cx
          self.y = cy
          
      def drawCell(self):
          draw.point(self.x, self.y)

#generate initial grid          
def gen_grid(sizex, sizey):
    for y in xrange(sizey):
        for x in xrange(sizex):
            cellstack.append(Cell(0, 0, x, y))
'''
#check if cell has been visited                
def visit_check(cell):
    if cell.visited == 0:
        neighbor_get(cell)
        cell.visited = 1
    else:
        cell.drawCell()
        return
     

#get random neighbor cell    
def neighbor_get(ccell):
    currentcell = Cell(0,0,0,0)
    for cell in cellist:
       if cell.x == (ccell.x + 1 or ccell.x - 1 or ccell.y + 1 or ccell.y - 1) and ccell.visited == 0:
            currentcell = cell
    if currentcell:
        visit_check(currentcell)
    else:
        return
'''        
def maze_iterative():
    while cellstack:
        ccell = cellstack.pop()
        if ccell.visited == 0:
            ccell.visited = 1
            neighbor_check(ccell)
        if ccell.visited == 1:
            ccell.drawCell()
            
def neighbor_check(ccell):
    cellist = []
    for cell in cellstack:
       if cell.x == (ccell.x + 1 or ccell.x - 1 or ccell.y + 1 or ccell.y - 1) and ccell.visited == 0:
           cellist.append(cell)
    ccell = random.choice(cellist)
    return ccell
    
def main():
    gen_grid(10, 10)
    current = cellstack[2]   
    maze_iterative()
    #img.save("maze.png")
    
main()