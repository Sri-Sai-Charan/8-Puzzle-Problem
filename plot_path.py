#!/usr/bin/python3
import numpy as np
class BFS_CLASS:
    def __init__(self, Visited, Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes,Future_State):
        self.Visited = Visited
        self.Node_State_I = Node_State_I
        self.Node_Index_I = Node_Index_I
        self.Parent_Node_Index_i = Parent_Node_Index_I
        self.Goal_Node = Goal_Node
        self.Open_Nodes = Open_Nodes
        self.Future_State = Future_State
        self.Goal_Check = False

def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

##Function to check if the next node is visited or not
def check_visited(my_data,Future_State):
    for ite in range(len(my_data.Visited)):
        if (my_data.Visited[ite]==Future_State).all():
            return False
        else:
            my_data.Visited.append(Future_State.copy())
            return True


def check_goal(my_data):
    if my_data.Node_State_I==my_data.Goal_Node:
        print("Goal Reached")
        my_data.Goal_Check = True
        return True
    else: 
        return False

def check_valid_state(my_data):
    current_array = np.array(my_data.Node_State_I.copy())
    pos = np.argwhere(current_array==0)
    if pos.size == 0:
        print("Not a Valid State")
        return False
    else:
        return True

def locate_zero(my_data):
    current_array = np.array(my_data.Node_State_I.copy())
    pos = np.argwhere(current_array==0)
    if pos.size == 0:
        print("Not a Valid State")
    else:
        return pos[0,0],pos[0,1]

def pop_func(my_data):
    my_data.Open_Nodes.reverse()
    my_data.Open_Nodes.pop()
    my_data.Open_Nodes.reverse()

def check_neighbour(my_data):
    i,j = locate_zero(my_data)
    if (j-1)>=0:
        check_future_state(my_data,i,j-1)
    if (i-1)>=0:
        check_future_state(my_data,i-1,j)
    if (j+1)<3:
        check_future_state(my_data,i,j+1)
    if (i+1)<3:
        check_future_state(my_data,i+1,j)

    my_data.Open_Nodes.pop(0)
    my_data.Node_State_I = my_data.Open_Nodes[0].copy()
    check_goal(my_data)
    return 0

def check_future_state(my_data,i,j):
    ix,jx = locate_zero(my_data)
    arr=np.array(my_data.Node_State_I)
    Future_State = arr.copy()
    val1=Future_State[i][j]
    val2=Future_State[ix][jx]
    Future_State[i][j] = val2
    Future_State[ix][jx]=val1

    if check_visited(my_data,Future_State):
        my_data.Open_Nodes.append(Future_State.tolist())

    
def bfs_search(my_data):
    if check_valid_state(my_data):
        while my_data.Goal_Check==False:
            check_neighbour(my_data)
    else:
        print("Invalid Start Node")

    return 0

def main():
    # fname = 'nodePath.txt'
    # data = np.loadtxt(fname) 
    Node_State_I= [[1,4,7],
                   [5,0,8],
                   [2,3,6]]
    Visited_States = [[1,4,7],
                   [5,0,8],
                   [2,3,6]]
    Goal_Node = [[1,4,7 ],[2,5,8],[3,6,0]]
    Parent_Node_Index_I = 1
    Node_Index_I = 0
    Open_Nodes = [[[1,4,7],
                   [5,0,8],
                   [2,3,6]]]
    my_data = BFS_CLASS(Visited_States,Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes,[])
    bfs_search(my_data)

if __name__ == '__main__':
    main()