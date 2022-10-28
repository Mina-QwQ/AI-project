from collections import deque

def read_file(file_name):
     f = open(file_name, 'r')
     W = float(f.readline())
     f.readline()
     current = [f.readline().split() for _ in range(4)]
     f.readline()
     goal = [f.readline().split() for _ in range(4)]
     return W, current, goal


def generate_fn(current, W):

    return


def insert_sort(val, lst):
    return 


def expand(current):
    return

class node():
    def __init__(self, previous, val, fn, gn):
        self.previous = previous
        self.val = val
        self.fn = fn
        self.gn = gn
        
def Graph_A_star(W, current, goal):
    current = node(None, current, generate_fn(current), 0)
    priority = deque() # our priority queue
    reached = [] # nodes that we have reached
    root = current
    while current.val != goal:
        # if we didn't reach goal
        if current.val in reached:
            current = priority.popleft()
            continue
        reached.append(current.val)
        next_nodes = expand(current) # expand current node
        for node in next_nodes: # put child nodes in priority queue
            tree_node = node(current, node, generate_fn(node), current.gn + 1) 
            insert_sort(tree_node, priority)
        current = priority.popleft()
    return # when we finished searching
    
W, current, goal = read_file(input()) # read input file from terminal
Graph_A_star(W, current, goal, priority, reached)

