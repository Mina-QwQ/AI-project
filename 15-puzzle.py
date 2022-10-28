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



def insert_sort(val, lst):



def expand(current):


class node():
    def __init__(self, previous, val, fn):
        self.previous = previous
        self.val = val
        self.fn = fn
        
def Graph_A*(W, current, goal):
    current = node(None, current, generate_fn(current))
    priority = deque() # our priority queue
    reached = [] # nodes that we have reached
    root = node()
    while !((current.val == goal) or (current.val in reached)):
        # if we didn't reach goal
        reached.append(current.val)
        next_nodes = expand(current) # expand current node
        for node in next_nodes: # put child nodes in priority queue
            tree_node = node(current, node, generate_fn(node))
            insert_sort(tree_node, priority)
        current = priority.popleft()
    return # when we finished searching
    
W, current, goal = read_file(input()) # read input file from terminal
Graph_A*(W, current, goal, priority, reached)

