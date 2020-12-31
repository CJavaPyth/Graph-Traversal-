#===================Import Libraries===================================================================
import pandas as pd
import random

#===================User defined variables============================================================
#File1 to be read
file1 = "roadNet-PA.txt"
file_separation_type = "\t"

#Number of hospitals (will be randomly generated)
hospno = 500
#File2 Hospital
file2 = "hospital_test.txt"

#File to write generated Graph dictionary
output_Graph_dict_file = "Graph_test.txt"

#===================Read text file=====================================================================
data = pd.read_csv(file1, sep = file_separation_type, header = None)
data.columns = ["from_node","to_node"]
number_of_nodes = max(max(data["from_node"]), max(data["to_node"]))+1
number_of_edges = data['from_node'].count()

#===================Generate random goal hospitals in File 2==============================================================================
list1 = random.sample(range(number_of_nodes), hospno)
list1 = [str(i) + '\n' for i in list1]

hosp_txt = open(file2, 'w+')
hosp_txt.writelines('# '+str(len(list1))+'\n')
hosp_txt.writelines(list1)
hosp_txt.close()

#Get hospital lists from file2
with open(file2) as f:
    lines = [line.rstrip() for line in f]
lines.pop(0)
hospitals = list(map(int, lines))
print('Hospitals are: ', hospitals)

#===================Creating adjacency list==============================================================================
#Expected graph adjacency list output, where [k(n)] is the list of neighbours of node k
#graph = [[0(n)],
#         [1(n)],
#         [2(n)]...]

graph = []
for i in range (number_of_nodes):
    graph.append([])
for i in range(number_of_edges) :
    source = data.iloc[i,0]
    target = data.iloc[i,1]    
    graph[source].append(target)


#removing duplicates from the graph in case there is any
for i in graph:
    i = list (dict.fromkeys(i))
print("graph generated")
    
#====================Creating Graph dictionary=============================================================================
#Expected Graph_dict output:
#Graph = {0:{"Goal": True, "Visited": False, "Neighbours" = 0(n)},
#         1:{"Goal": False, "Visited": False, "Neighbours" = 1(n)},
#         2:...}

Graph = {}
Dict = {}

for i in range (number_of_nodes):
    #Create an empty dictionary for each node
    Graph[i] = Dict
    #Update Dict key:value pairs for each node
    Dict["Goal"] = False
    Dict["Visited"] = False
    Dict["Neighbours"] = graph[i]
    #Update Dict["Goal"] to true if the node is a hospital
    for j in hospitals:
        if i == j:
            Dict["Goal"] = True
    #Reset Dict to empty
    Dict = {}
print("Graph dict generated")

#====================Check console output for updated Goal value & structure of Graph============================================================================
#"Goal" boolean for should be true
print(Graph[hospitals[0]])

#"Goal" boolean for non-goal hospitals - False(some random hospitals, hopefully not goal!)
print(Graph[0])
print(Graph[50])

###====================Output generated Graph Dictionary=========================================================
##graph_txt = open(output_Graph_dict_file,"w+")
##for i in range (number_of_nodes):
##    graph_txt.writelines(str(i) + str(Graph[i]) + "\n\n")
##graph_txt.close()
##print("Output to txt file done")
