import numpy as np
# import sys
# sys.version
# '2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)]'

class BFS_CLASS:
    def __init__(self, queue, Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes):
        self.Visited_Queue = queue
        self.Node_State_I = Node_State_I
        self.Node_Index_I = Node_Index_I
        self.Parent_Node_Index_i = Parent_Node_Index_I
        self.Goal_Node = Goal_Node
        self.Open_Nodes = Open_Nodes
        
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

def check_visited(my_data):
    for ite in range(len(my_data.Visited_Queue)):
        if my_data.Visited_Queue[ite] == my_data.Node_State_I:
            return True
        else:
            my_data.Visited_Queue.append(my_data.Node_State_I[int((len(my_data.Node_State_I)/3)-1)])
            return False, my_data.Visited_Queue


def check_goal(my_data):
    if my_data.Node_State_I.top()==my_data.goal_state:
        return True
    else: 
        return False

def check_neighbour():
   
    # if east -  #check visited - move - update open nodes (add parent index and child index)
    #if north  #check visited - move - update open nodes (add parent index and child index)
    # if west  #check visited - move - update open nodes (add parent index and child index)
    # if south  #check visited -move - update open nodes (add parent index and child index)
    # move to parent    
         
    return 0

def move_forward(my_data,direction):
    if direction == 0:
        # north 
        return 0
    # if south
    #if east
    #if west 
    #if parent - close parent in queue - new parent in queue

        



def bfs_search(my_data):
    if check_goal(my_data) != True:
        if check_neighbour(my_data) != True:
            # decide direction
            move_forward(my_data)


    


    


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
            
    
    Visited_States = [[1,4,7],[5,0,8],[2,3,6]]
    Visited_States.append(Visited_States)
    Goal_Node = np.array([[1,4,7 ],[2,5,8],[3,6,0]])
    Node_State_I= np.array([[1,4,7],[5,0,8],[2,3,6]])
    Parent_Node_Index_I = 0
    Node_Index_I = Parent_Node_Index_I
    Open_Nodes = []
    my_data = BFS_CLASS(Visited_States,Node_State_I,Node_Index_I,Parent_Node_Index_I,Goal_Node,Open_Nodes)
    # bfs_search(my_data)
    print(my_data.Visited_Queue)




if __name__ == '__main__':
    main()