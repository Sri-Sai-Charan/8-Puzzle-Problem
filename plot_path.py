#!/usr/bin/python3
import sys
import numpy as np
# import sys
# sys.version
# '2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)]'
# sys.set_option('display.max_colwidth', None)
class BFS_CLASS:
    def __init__(self, Visited, Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes):
        self.Visited = Visited
        self.Node_State_I = Node_State_I
        self.Node_Index_I = Node_Index_I
        self.Parent_Node_Index_i = Parent_Node_Index_I
        self.Goal_Node = Goal_Node
        self.Open_Nodes = Open_Nodes
        self.Future_State = Node_State_I
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

def check_visited(my_data):
    for ite in range(len(my_data.Visited)):
        #If state is not visited then add to visited and return false
        if my_data.Visited[ite]==my_data.Node_State_I:
            return True
        else:
            my_data.Visited.append(my_data.Node_State_I)
            return False


def check_goal(my_data):
    if my_data.Node_State_I==my_data.Goal_Node:
        print("Goal Reached")
        return True
    else: 
        return False

def locate_zero(my_data):
    current_array = np.array(my_data.Node_State_I)
    pos = np.argwhere(current_array==0)
    if pos.size == 0:
        print("Not a Valid State")
    else:
        return pos[0,0],pos[0,1]

def check_neighbour(my_data):
    i,j = locate_zero(my_data)
    if (i-1)>=0:
        #check v and move
        set_future_state(my_data)
        check_visited(my_data) 
    if (i+1)<3:
        check_visited(my_data)
    if (j-1)>=0:
        check_goal(my_data)

    if (j+1)<3:
        check_goal(my_data)
    # if east -  #check visited - move - update open nodes (add parent index and child index)
    #if north  #check visited - move - update open nodes (add parent index and child index)
    # if west  #check visited - move - update open nodes (add parent index and child index)
    # if south  #check visited -move - update open nodes (add parent index and child index)
    # move to parent    
         
    return 0

def set_future_state(my_data,i,j):
    my_data.Future_State = my_data.Node_State_I
    my_data.Future_State[i][j]

    # if south
    #if east
    #if west 
    #if parent - close parent in queue - new parent in queue

        



def bfs_search(my_data):
    # if check_goal(my_data) == False:
    #     if check_neighbour(my_data) != True:
            # decide direction
            # move_zero(my_data)
    return 0

    


    


def main():
    # fname = 'nodePath.txt'
    # data = np.loadtxt(fname)

    # if len(data[1]) is not 9:
    #     print("Format of the text file is incorrect, retry ")
    # else:
    #     for i in range(0, len(data)):
    #         if i == 0:
    #             print("Start Node")
    #         elif i == len(data)-1:
    #             print("Achieved Goal Node")
    #         else:
    #             print("Step ",i)
            # print_matrix(data[i])
            
    # Node_State_I= np.array([[[1,4,7],
    #                [5,0,8],
    #                [2,3,6]]])
    Node_State_I= [[1,4,7],
                   [5,0,8],
                   [2,3,6]]
    Visited_States = [Node_State_I]
    # np.append(Visited_States,[[1,4,7],
    #                [5,0,8],
    #                [2,3,6]])
    # Visited_States.append([[1,5,7],
    #                [5,0,8],
    #                [2,3,6]])
    Goal_Node = Node_State_I
    Parent_Node_Index_I = 0
    Node_Index_I = Parent_Node_Index_I
    Open_Nodes = []
    my_data = BFS_CLASS(Visited_States,Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes)
    bfs_search(my_data)



if __name__ == '__main__':
    main()