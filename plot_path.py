#!/usr/bin/python3
import numpy as np
class BFS_CLASS:
    def __init__(self, Visited, Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes):
        self.Visited = Visited
        self.Node_State_I = Node_State_I
        self.Node_Index_I = Node_Index_I
        self.Parent_Node_Index_i = Parent_Node_Index_I
        self.Goal_Node = Goal_Node
        self.Open_Nodes = Open_Nodes
        self.Goal_Check = False
        self.count_parent = 1
        self.count_node = 1
        self.step_count = 0
def print_matrix(state,my_data):
    my_data.step_count+=1
    print("Step :",my_data.step_count)
    print("-------------")
    
    for row in range(0, 3):
        for col in range(0, 3):
            if col == 0:
                print("|", end=" ")
            print(state[row][col], "|", end=" ")
        print('\n-------------')
    print("\n--\n")

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

def check_neighbour(my_data):
    check_left(my_data)
    check_top(my_data)
    check_right(my_data)
    check_bottom(my_data)
    back_track(my_data)
    check_goal(my_data)
    return 0

def check_left(my_data):
    i,j = locate_zero(my_data)
    if (j-1)>=0:
        check_future_state(my_data,i,j-1)

def check_top(my_data):
    i,j = locate_zero(my_data)
    if (i-1)>=0:
        check_future_state(my_data,i-1,j)

def check_right(my_data):
    i,j = locate_zero(my_data)
    if (j+1)<3:
        check_future_state(my_data,i,j+1)

def check_bottom(my_data):
    i,j = locate_zero(my_data)
    if (i+1)<3:
        check_future_state(my_data,i+1,j)

def back_track(my_data):
    my_data.count_parent+=1
    my_data.Open_Nodes.pop(0)
    my_data.Node_State_I = my_data.Open_Nodes[0].copy()

def check_future_state(my_data,i,j):
    ix,jx = locate_zero(my_data)
    arr=np.array(my_data.Node_State_I)
    Future_State = arr.copy()
    Future_State[i][j],Future_State[ix][jx] = Future_State[ix][jx], Future_State[i][j]

    if check_visited(my_data,Future_State):
        my_data.Open_Nodes.append(Future_State.tolist())
        my_data.count_node+=1
        my_data.Node_Index_I.append(my_data.count_node)
        my_data.Parent_Node_Index_i.append(my_data.count_parent)
    
def bfs_search(my_data):
    if check_valid_state(my_data):
        while my_data.Goal_Check==False:
            check_neighbour(my_data)
        generate_path(my_data)
    else:
        print("Invalid Start Node")

    return 0

def generate_path(my_data):
    idxb = np.array([[-1]])
    idxa = np.array([[-1]])
    b = np.array(my_data.Node_Index_I)
    a = np.array(my_data.Parent_Node_Index_i)
    path_list = []
    # path_list.append(b[-1])
    while True:
        idxa = np.argwhere(b==a[idxa[0,0]])
        idxb = np.argwhere(b==a[idxb[0,0]])
        if idxb > 0 :
            path_list.append(b[idxb[0,0]])
        else:
            path_list.append(b[0])
            break
    path_list.reverse()
    path_values = []
    for ite in range(len(path_list)-1):
        path_values.append(my_data.Visited[path_list[ite]-1])
    path_values.append(my_data.Goal_Node)

    for ite in range(0,(len(path_values))):
        print_matrix(path_values[ite],my_data)
def main():
    Node_State_I= [[1,4,7],[5,0,8],[2,3,6]]
    Goal_Node = [[1,4,7],[2,5,8],[3,6,0]]

    Visited_States = [Node_State_I.copy()]
    Open_Nodes = [[Node_State_I.copy()]]
    my_data = BFS_CLASS(Visited_States,Node_State_I,[1],[1],Goal_Node,Open_Nodes)
    bfs_search(my_data)

if __name__ == '__main__':
    main()