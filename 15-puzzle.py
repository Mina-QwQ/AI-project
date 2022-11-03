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
     f = open(file_name, 'r')
     W = float(f.readline())
     f.readline()
     current = [f.readline().split() for _ in range(GRID_SIZE)]
     f.readline()
     goal = [f.readline().split() for _ in range(GRID_SIZE)]
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
    for h in range(row-1, row+2): 
        if h < 0 or h >= GRID_SIZE or h == row: #if not valid for 0 to move to
            continue
        child = copy.deepcopy(current.board)
        child[row][col], child[h][col] = child[h][col], child[row][col]
        children.append(child)
    for v in range(col-1, col+2):
        if v < 0 or v >= GRID_SIZE or v == col: #if not valid for 0 to move to
            continue 
        child = copy.deepcopy(current.board)
        child[row][col], child[row][v] = child[row][v], child[row][col]
        children.append(child)
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
    def __init__(self, previous, board, fn, gn):
        self.previous = previous
        self.board = board
        self.fn = fn
        self.gn = gn


def Graph_A_star(W, current, goal):
    current = node(None, current, generate_fn(current, goal, W, 0), 0)
    priority = deque() # our priority queue
    reached = [] # nodes that we have reached
    root = current
    while current.board != goal:
        # if we didn't reach goal
        if current.board in reached:
            current = priority.popleft()
            continue
        reached.append(current.board)
        children = expand(current) # expand current node
        for child in children: # put child nodes in priority queue
            child_node = node(current, child, generate_fn(child, goal, W, current.gn+1), current.gn + 1) 
            insert_sort(child_node, priority)
        current = priority.popleft()
    return current # when we finished searching
    
W, current, goal = read_file(input()) # read input file from terminal
result = Graph_A_star(W, current, goal)
soln_path = []
while result != None:
    soln_path.insert(0, result)
    result = result.previous

for soln_node in soln_path:
    for row in soln_node.board:
        print(row)
    print('\n')
