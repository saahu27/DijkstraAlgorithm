import numpy as np
import collections 
import os

#definition of node
class Node:
    #all the information about how the node got here, will be stored. thus every node we generate will be made an object.
    def __init__(self, node_index, node_data,parent_node,parent_node_index, next_actionfrom_parent, cost):
        self.node_index = node_index
        self.node_data = node_data
        self.parent_node = parent_node
        self.parent_node_index = parent_node_index
        self.next_actionfrom_parent = next_actionfrom_parent
        self.cost = cost


# Getting input node
def get_input():
    print("If your matrix looks like this: [1,4,7],[5,0,8],[2,3,6] then please enter the numbers column wise, so for the above number")
    print("enter number as : 152403786 for the goal state [1,4,7 ],[2,5,8],[3,6,0")
    print("\nEnter the input node column wise wize(only enter numbers between 0 to 8): \n ")
    input_node = []
    for i in range(9):
        node_value = int(input()) 
        #node_value = int(input("Enter the " + str(i + 1) + " indexber: " + "\n"))
        #if node_value not in [0,1,2,3,4,5,6,7,8]:
        if node_value < 0 or node_value > 8:
            print("Only enter numbers which are between [0-8]")
            exit(0)
        else:
            input_node.append(node_value)
            #input_node[i] = np.array(node_value)
    return np.reshape(input_node, (3, 3))

#checking how many inversions are there. 
# how many smaller numbers are there to the right of number is the number of inversions
def Check_Solvability(input_node):
    input_node = np.reshape(input_node, 9)
    inversions = 0
    for i in range(len(input_node)): 
        for j in range(i + 1, len(input_node)): 
            if (input_node[i] > input_node[j] and input_node[i]!=0 and input_node[j]!=0): 
                inversions += 1
    if inversions % 2 == 0:
        return ("True")
    else:
        print("There is no solution")
        exit(0)

# To Find the location of blank tile
def blank_tile_location(current_node):
    i, j = np.where(current_node == 0)
    # for i in range(0,len(current_node)):
    #     for j in range(0,len(current_node)):
    #         if(current_node[i][j] == 0):
    #             return i,j
    return i, j

def Actionmove_left(current_node):
    i, j = blank_tile_location(current_node)
    if j == 0:  # If already in leftmost column
        return None
    else:   # Moving left by storing left node value in temp
        next_node = np.copy(current_node)
        left_value = next_node[i, j - 1] 
        next_node[i, j] = left_value
        next_node[i, j - 1] = 0
        return next_node

def Actionmove_right(current_node):
    i, j = blank_tile_location(current_node)
    if j == 2:   # If already in rightmost column
        return None
    else:   # Moving right by storing right node value in temp
        next_node = np.copy(current_node)
        right_value = next_node[i, j + 1]
        next_node[i, j] = right_value
        next_node[i, j + 1] = 0
        return next_node

def Actionmove_up(current_node):
    i, j = blank_tile_location(current_node)
    if i == 0:   # If already in top row
        return None
    else:  # Moving up by storing up node value in temp
        next_node = np.copy(current_node)
        up_value = next_node[i - 1, j]
        next_node[i, j] = up_value
        next_node[i - 1, j] = 0
        return next_node

def Actionmove_down(current_node):
    i, j = blank_tile_location(current_node)
    if i == 2:  # If already in bottom row
        return None
    else:   # Moving down by storing node node value in temp
        next_node = np.copy(current_node)
        down_value = next_node[i + 1, j]
        next_node[i, j] = down_value
        next_node[i + 1, j] = 0
        return next_node

#perform the move
def Next_Node(move,node_data):

    if move == 'Left':
        return Actionmove_left(node_data)
    elif move == 'Right':
        return Actionmove_right(node_data)
    elif move == 'Up':
        return Actionmove_up(node_data)
    elif move == 'Down':
        return Actionmove_down(node_data)
    else:
        return None

def CreateKey(node_data):
    index_array = np.reshape(node_data, 9)
    index_string = int(''.join(str(i) for i in index_array))
    return index_string

def BFS(input_node,goal_node):
    actions = ["Left", "Right","Up","Down"]
    visited_nodes = []
    visited_nodes.append(input_node)
    #adding input node as list to the queue
    input_node = collections.deque([input_node])
    nodes_tobe_visitedlist = {CreateKey(input_node[0].node_data) : input_node[0].node_index}
    
    node_index = 0

    while input_node: #while queue is not empty
        current_node = input_node.popleft() #poping the first element in the queue
        if current_node.node_data.tolist() == goal_node.tolist(): #checking if its the gooal state if yes return current node and all the visited nodes
            print("Goal state found")
            return current_node,visited_nodes
        
        for move in actions: #exploring every action state for each node state
            next_node_data = Next_Node(move,current_node.node_data) #getting the next node by taking an action
            #None is returned if an action is not possible from a state
            if next_node_data is not None :
                next_node = Node(0,np.array(next_node_data),current_node,0,move,0) #creating object instance for the next node

                # if any(x.node_data.tolist() == next_node.node_data.tolist() for x in visited_nodes) == False :
 #checking if the node is already in the queue by a dictionary
 # we can also use visited node list as above line which is commented for checking. But thought searching for a key is much faster
                if CreateKey(next_node.node_data) not in nodes_tobe_visitedlist : 
                    node_index += 1
                    next_node.node_index = node_index 
                    next_node.parent_node_index = node_index - 1
                    input_node.append(next_node) #if not viisted adding to the queue and vissited list
                    nodes_tobe_visitedlist[CreateKey(next_node.node_data)] = next_node.node_index
                    visited_nodes.append(next_node)

                    if next_node.node_data.tolist() == goal_node.tolist(): #if its a goal state exiting
                        print("Goal state found")
                        return next_node,visited_nodes

    return None,None

def Generate_Path(goal_node):  
    path = []  
    path.append(goal_node) #appending goal node to the path
    parent_node = goal_node.parent_node  #taking the parent node of the goal node
    while parent_node is not None: #if the parent node is none it is the input node.
        path.append(parent_node) #if not none adding to the path
        temp = parent_node.parent_node #taking the parent node of the parent node thus back travcking
        parent_node = temp
    return list(reversed(path)) #returning a path with reverse that is from input to the goal node.


# Printing final states
def print_matrix(final_list):
    print("Printing the final solution and also the path to the required node \n")
    for l in final_list:
        print("Node No.:  " + str(l.node_index) + "\n" + "Action performed : " + str(l.next_actionfrom_parent) + "\n" + "Resulting Node :" + "\n" + str(l.node_data))

# Text file edit for path
def path_textfile(path_formed):
    if os.path.exists("nodePath.txt"):   # Checking the existence of textfile and removing it
        os.remove("nodePath.txt")

    f = open("nodePath.txt", "a")
    for node in path_formed:    # Rewriting the textfile with path found
        if node.parent_node is not None:
            f.write(str(node.node_index) + "\t" + str(node.parent_node.node_index) + "\t" + str(node.cost) + "\n")
    f.close()

# Text file edit of all node
def allnodes_textfile(visited_nodes):
    if os.path.exists("Nodes.txt"):     # Checking existence of textfile and removing it
        os.remove("Nodes.txt")

    f = open("Nodes.txt", "a")
    for node in visited_nodes:
        f.write('[')
        for i in range(0,len(node.node_data)):
            for j in range(len(node.node_data)):
                f.write(str(node.node_data[j][i]) + " ")
        f.write(']')
        f.write("\n")
        # f.write(str(node.node_data.tolist()) + "\n")
    f.close()

# Text file edit of node info
def nodeinfo_textfile(visited):
    if os.path.exists("NodesInfo.txt"):     # Checking existence of textfile and removing it
        os.remove("NodesInfo.txt")

    f = open("NodesInfo.txt", "a")
    for n in visited:       # Rewriting the textfile with the node info
        if n.parent_node is not None:
            f.write(str(n.node_index) + "\t" + str(n.parent_node.node_index) + "\t" + str(n.cost) + "\n")
    f.close()

def main():
    input_node = get_input() #getting the input matrix
    boolean = Check_Solvability(input_node) #checking if puzzle is solvable or not

    if boolean == "True": 
        input_node = input_node.T
        print("The input node looks like this",input_node)
        input_node = Node(0,input_node,None,None,0,0) #object instace of input node also named inpu node
        goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
        goal_node,visited_nodes = BFS(input_node,goal_state.T) #started BFS search and returns final goal state and all the visitednodes list
        print(goal_node.node_data)
        if goal_node.node_data is not None and visited_nodes is not None:
            shortest_path = Generate_Path(goal_node) #calling generate path to back track the path to the input node from goal

            print("\n The shortest path to reach the goal is: ")
            for node in shortest_path:
                print("\n")
                print(node.node_data)

    print_matrix(shortest_path) #printing the shortest path
    path_textfile(shortest_path) #shortest path nodes text file
    allnodes_textfile(visited_nodes) #all the nodes visited as text file
    nodeinfo_textfile(visited_nodes) #childnode index parent node idex and cost of the move.


if __name__ == "__main__":
    main()








            


    

        
