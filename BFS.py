#===========================CX2001 Algorithms Project 2==================================================
print("Welcome to Group 1 Project 2!")
      
#===========================Import Libraries=========================================================
import Lab_2_create_a_graph
from Lab_2_create_a_graph import Graph
from Lab_2_create_a_graph import graph
from Lab_2_create_a_graph import number_of_nodes
import collections
from collections import deque

#===========================User defined variables==================================================
#Output files to write into
part_a_output_file = "part_a_PA_500hosp.txt"
part_c_output_file = "part_c_PA_500hosp.txt"
part_d_output_file = "part_d_PA_500hosp.txt"

#For part_d only!
k_hosp = 4

#===========================Part_a========================================================
def BFS_shortest_path_part_a(Graph, start):
    #L
    k = 1et k be the top number of nearest hospitals to be found
    #nodes to be tracked
    queue = collections.deque([[start]])
    #store visited nodes to avoid going through each node twice
    visited = set()
    #store shortest path(s) to k hospitals
    store = collections.deque()
    #store distance of shortest path(s)
    store_dist = []

    #if start is goal
    if (Graph[start]).get("Goal") == True:
        #print("This is a hospital!")
        return ("This is a hospital!")

    #loop till queue is empty
    while (queue):
        #pop first path from queue (path is a list of nodes)
        path = queue.popleft()
        #get last node from path
        node = path[-1]
        #identify neighbours linked to the node
        neighbours = graph[node]
        #go through all neighbour nodes, construct a new path
        #add neighbours of node to queue
        for neighbour in neighbours:
            #Check if neighbour has been visited
            if neighbour not in visited:
                #mark neighbour as visited
                visited.add(neighbour)
                new_path = collections.deque(path)
                new_path.append(neighbour)
                queue.append(new_path)
                #access Graph Dict to check if hospital is found
                if (Graph[neighbour]).get("Goal") == True:
                    distance = len(new_path) - 1
                    #append the shortest k - path(s) to a new storage list 
                    store.append(new_path)
                    #append the shortest k - path(s) to a new storage list
                    store_dist.append(distance)
                    #check if we have found k hospitals, return k-paths and their distances
                    if len(store) == k:
                         return (store, store_dist)
    
    #If cannot find hospital
    return ("No path exists")

#==============================Output for Part_a=============================================================#
print("Start output part_a")
part_a_txt = open(part_a_output_file,"w+")
part_a_txt.write ("Output shortest path, distance of nearest hospital from each note:\n\n")
for i in range (number_of_nodes):
    part_a_txt.writelines("From node " + str(i) + ": ")
    part_a_txt.writelines(str(BFS_shortest_path_part_a(Graph,i)) + "\n")
part_a_txt.close()
print("Output part_a completed")

#==============================Part_c=============================================================#
def BFS_shortest_path_part_c(Graph, start):
    #Let k be the top number of nearest hospitals to be found
    k = 2
    #nodes to be tracked
    queue = collections.deque([[start]])
    #store visited nodes to avoid going through each node twice
    visited = set()
    #store shortest path(s) to k hospitals
    store = collections.deque()
    #store distance of shortest path(s)
    store_dist = []

    #if start is goal
    if (Graph[start]).get("Goal") == True:
        return ("This is a hospital!")

    #loop till queue is empty
    while (queue):
        #pop first path from queue (path is a list of nodes)
        path = queue.popleft()
        #get last node from path
        node = path[-1]
        #identify neighbours linked to the node
        neighbours = graph[node]
        #go through all neighbour nodes, construct a new path
        #add neighbours of node to queue
        for neighbour in neighbours:
            #Check if neighbour has been visited
            if neighbour not in visited:
                #mark neighbour as visited
                visited.add(neighbour)
                new_path = collections.deque(path)
                new_path.append(neighbour)
                queue.append(new_path)
                #access Graph Dict to check if hospital is found
                if (Graph[neighbour]).get("Goal") == True:
                    distance = len(new_path) - 1
                    #Get hospital node from the shortest path
                    new_path_hosp = new_path[-1]
                    #append the shortest k - hospitals  to a new storage list 
                    store.append(new_path_hosp)
                    #append the shortest k - path(s) to a new storage list
                    store_dist.append(distance)
                    #check if we have found k hospitals, return k-paths and their distances
                    if len(store) == k:
                         return (store, store_dist)
                
    #If cannot find hospital
    return ("No path exists")

#=========================Output part_c=======================================================================#
print("Start output part_c")
part_c_txt = open(part_c_output_file,"w+")
part_c_txt.write ("Output shortest path, distance of top-2 nearest hospital from each note:\n\n")
for i in range (number_of_nodes):
    part_c_txt.writelines("From node " + str(i) + ": ")
    part_c_txt.writelines(str(BFS_shortest_path_part_c(Graph,i)) + "\n")
part_c_txt.close()
print("Output part_c completed")

#==========================Part_d=================================================================#
#Part d - define k in line 3 of function "BFS_shortest_path_part_d(graph, start, k)"
def BFS_shortest_path_part_d(Graph, start, k):
    #nodes to be tracked
    queue = collections.deque([[start]])
    #store visited nodes to avoid going through each node twice
    visited = set()
    #store shortest path(s) to k hospitals
    store = collections.deque()
    #store distance of shortest path(s)
    store_dist = []

    #if start is goal
    if (Graph[start]).get("Goal") == True:
        return ("This is a hospital!")

    #loop till queue is empty
    while (queue):
        #pop first path from queue (path is a list of nodes)
        path = queue.popleft()
        #get last node from path
        node = path[-1]
        #identify neighbours linked to the node
        neighbours = graph[node]
        #go through all neighbour nodes, construct a new path
        #add neighbours of node to queue
        for neighbour in neighbours:
            #Check if neighbour has been visited
            if neighbour not in visited:
                #mark neighbour as visited
                visited.add(neighbour)
                new_path = collections.deque(path)
                new_path.append(neighbour)
                queue.append(new_path)
                #access Graph Dict to check if hospital is found
                if (Graph[neighbour]).get("Goal") == True:
                    distance = len(new_path) - 1
                    #Get hospital node from the shortest path
                    new_path_hosp = new_path[-1]
                    #append the shortest k - hospitals  to a new storage list 
                    store.append(new_path_hosp)
                    #append the shortest k - path(s) to a new storage list
                    store_dist.append(distance)
                    #check if we have found k hospitals, return k-paths and their distances
                    if len(store) == k:
                         return (store, store_dist)
                
    #If cannot find hospital
    return ("No path exists")

#==========================Output part_d================================================#
print("Start output part_d")
part_d_txt = open(part_d_output_file,"w+")
part_d_txt.write ("Output shortest path, distance of top-k nearest hospital from each note:\n\n")
for i in range (number_of_nodes):
    part_d_txt.writelines("From node " + str(i) + ": ")
    part_d_txt.writelines(str(BFS_shortest_path_part_d(Graph,i,k_hosp)) + "\n")
part_d_txt.close()
print("Output part_d completed")

#===========================Program Ends!================================================================#
print("Program ended!")
