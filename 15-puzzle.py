from collections import deque
import copy

GRID_SIZE = 4 

"""
reads in input file
params:
string file_name 
returns:
numeric W, 2D array current, 2D array goal
"""
def read_file(file_name):
     print(file_name)
     f = open(file_name, 'r')
     W = float(f.readline())
     f.readline()
     current = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(GRID_SIZE)]
     f.readline()
     goal = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(GRID_SIZE)]
     f.close()
     return W, current, goal

"""
generates f(n) = g(n) + W * h(n)
params:
2D array current, 2D array goal, W numeric, gn numeric
returns: 
fn numeric
"""
def generate_fn(current, goal, W, gn):

    hn = 0
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE): #for each value 
            if current[r][c] == '0': #board unit with no number
                continue
            num = current[r][c] #current number 
            
            #find row and col of val in goal 
            for r2 in range(GRID_SIZE):
                for c2 in range(GRID_SIZE):
                    if goal[r2][c2] == num:
                        goal_r, goal_c = r2, c2
                        break
            hn += max(abs(goal_r - r), abs(goal_c -c))     
    fn = gn + W * hn
    return fn

"""
expands given state node 
params:
node Object current
returns:
array of 2D array successors
"""
def expand(current):
    
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE): 
            if current.board[r][c] == '0': #find board unit with '0'
                row, col = r, c
                break
    children = []
    if row > 0:
        child = copy.deepcopy(current.board)
        child[row][col], child[row-1][col] = child[row-1][col], child[row][col]
        children.append((child, 'U'))
    if row < GRID_SIZE-1:
        child = copy.deepcopy(current.board)
        child[row][col], child[row+1][col] = child[row+1][col], child[row][col]
        children.append((child, 'D'))
    if col > 0:
        child = copy.deepcopy(current.board)
        child[row][col], child[row][col-1] = child[row][col-1], child[row][col]
        children.append((child, 'L'))
    if col < GRID_SIZE-1:
        child = copy.deepcopy(current.board)
        child[row][col], child[row][col+1] = child[row][col+1], child[row][col]
        children.append((child, 'R'))
    return children


"""
inserts given state node into frontier 
params:
node Object current_node
deque Object queue
returns:
deque Object queue
"""
def insert_sort(current_node, queue):
    index = 0
    for node in queue: 
        if current_node.fn < node.fn:
            break
        index += 1
    queue.insert(index, current_node)

"""
node Object to store critical data values of each state node 
data members:
parent node Object previous 
2D array board board
numeric fn
numeric gn
"""
class node():
    def __init__(self, previous, board, fn, gn, move):
        self.previous = previous
        self.board = board
        self.fn = fn
        self.gn = gn
        self.move = move


def Graph_A_star(W, current, goal):
    current = node(None, current, generate_fn(current, goal, W, 0), 0, None)
    N = 1
    priority = deque() # our priority queue
    reached = [] # nodes that we have reached
    root = current
    while current.board != goal:
        # if we didn't reach goal

        reached.append(current.board)
        children = expand(current) # expand current node
        for child in children: # put child nodes in priority queue
            if child[0] in reached:
                 continue
            child_node = node(current, child[0], generate_fn(child[0], goal, W, current.gn+1), current.gn + 1, child[1])
            N+=1
            insert_sort(child_node, priority)
        current = priority.popleft()
    return N, current # when we finished searching

filename = input("Filename: ")    
W, initial, goal = read_file(filename) # read input file from terminal
print(goal)

N, result = Graph_A_star(W, initial, goal)

f = open("result_"+filename, 'w')
read = open(filename, 'r')
read.readline() # read W
read.readline() # read space
line = read.readline()
while line != '':
     f.write(line)
     line = read.readline()

f.write('\n')
f.write(str(W)+'\n')

soln_path = []
moves = []
fn = []
d = 0
while result.board != initial:
    soln_path.insert(0, result)
    moves.insert(0, result.move)
    fn.insert(0, str(result.fn))
    result = result.previous
    d+=1
fn.insert(0, str(result.fn))

f.write(str(d)+'\n')
f.write(str(N)+'\n')
f.write(' '.join(moves)+'\n')
f.write(' '.join(fn))

f.close()

for soln_node in soln_path:
    for row in soln_node.board:
        print(row)
    print('\n')
