#===========================CX2001 Algorithms Project 2==================================================
print("Welcome to Group 1 Project 2!")
      
#===========================Import Libraries=========================================================
import Lab_2_create_a_graph_test
from Lab_2_create_a_graph_test import Graph
from Lab_2_create_a_graph_test import graph
from Lab_2_create_a_graph_test import number_of_nodes
import collections
from collections import deque
import timeit
import pandas as pd

#===========================User defined variables==================================================
#Output files to write into
part_a_output_file = "part_a_test.txt"
part_c_output_file = "part_c_test.txt"
part_d_output_file = "part_d_test.txt"

#For part_d only!
k_hosp = 4

#===========================Part_a========================================================
def BFS_shortest_path_part_a(Graph, start):
    #Let k be the top number of nearest hospitals to be found
    k = 1
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

                    #loop till new_path is empty
                    while (store[new_path]):
                        #pop first node in shortest path
                        #Got the shortest path for the next node in line
                        next_node_path = store.popleft()
                        #Get the next node
                        next_node = store[next_node_path[1]]
                        #set visited to true
                        Graph[next_node]['Visited'] = True
                    
                
                    #append the shortest k - path(s) to a new storage list
                    store_dist.append(distance)
                    #check if we have found k hospitals, return k-paths and their distances
                    if len(store) == k:
                         return (store, store_dist)
    
    #If cannot find hospital
    return ("No path exists")

#==============================Output for Part_a=============================================================#
print("Start output part_a")
data = []
for i in range(number_of_nodes):
    data.append([i,BFS_shortest_path_part_a(Graph,i)])
print("Data ran")

df = pd.DataFrame(data)
df.to_csv(part_a_output_file)

##part_a_txt = open(part_a_output_file,"w+")
##part_a_txt.write ("Output shortest path, distance of nearest hospital from each note:\n\n")
##for i in range (number_of_nodes):
##    part_a_txt.writelines("From node " + str(i) + ": ")
##    part_a_txt.writelines(str(BFS_shortest_path_part_a(Graph,i)) + "\n")
##part_a_txt.close()
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
##print("Start output part_c")
##part_c_txt = open(part_c_output_file,"w+")
##part_c_txt.write ("Output shortest path, distance of top-2 nearest hospital from each note:\n\n")
##for i in range (number_of_nodes):
##    part_c_txt.writelines("From node " + str(i) + ": ")
##    part_c_txt.writelines(str(BFS_shortest_path_part_c(Graph,i)) + "\n")
##part_c_txt.close()
##print("Output part_c completed")

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
##print("Start output part_d")
##part_d_txt = open(part_d_output_file,"w+")
##part_d_txt.write ("Output shortest path, distance of top-k nearest hospital from each note:\n\n")
##for i in range (number_of_nodes):
##    part_d_txt.writelines("From node " + str(i) + ": ")
##    part_d_txt.writelines(str(BFS_shortest_path_part_d(Graph,i,k_hosp)) + "\n")
##part_d_txt.close()
##print("Output part_d completed")

#=======================Runtime output================================================================
def timer(func,*args):
	start = timeit.default_timer()
	func(*args)
	stop = timeit.default_timer()
	print('Time: ', stop - start, '\n')

def a():
    for i in range (number_of_nodes):
        BFS_shortest_path_part_a(Graph,i)

def c():
    for i in range (number_of_nodes):
        BFS_shortest_path_part_c(Graph,i)

def d():
    for i in range (number_of_nodes):
        BFS_shortest_path_part_d(Graph,i,k_hosp)

print("Part_a runtime: ")
timer(a)
print("Part_b runtime: ")
timer(c)
print("Part_d runtime: ")
timer(d)

#===========================Program Ends!================================================================#
print("Program ended!")
