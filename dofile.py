# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 16:31:45 2016

FACEBOOK DATA BASE

@author: carrierclement
"""


#import pandas as pd
#data = pd.read_csv(filepath_or_buffer='facebook.spydata')



import networkx as nx
import matplotlib.pyplot as plt


G_fb = nx.read_edgelist("facebook.txt", create_using = nx.Graph(), nodetype = int)
print nx.info(G_fb)

#Create network layout for visualizations
spring_pos = nx.spring_layout(G_fb)

plt.axis("off")
nx.draw_networkx(G_fb, pos = spring_pos, with_labels = False, node_size = 15)



############### Community detection ###########
import community 
parts = community.best_partition(G_fb)
values = [parts.get(node) for node in G_fb.nodes()]


plt.axis("off")
nx.draw_networkx(G_fb, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 15, with_labels = False)
#plt.savefig(graph, format='png')


dict.values(parts)[2]
dict.keys(parts)

#dict.items(parts)
#wanted_keys = [1] # The keys you want

group1= [None] * 4039
i = 0
while i in G_fb.nodes():
    if dict.values(parts)[i]==1 : group1[i]=dict.keys(parts)[i]
    else: group1[i]=None
    i = i + 1


#import numpy as np
#new_a = np.delete(group1, [None])

G_1 = G_fb.subgraph(group1)
nx.draw_networkx(G_1, pos = spring_pos, cmap = plt.get_cmap("jet"), node_size = 15, with_labels = False)



group1_2= [None] * 4039
i = 0
while i in G_fb.nodes():
    if dict.values(parts)[i]==1:
        group1_2[i]=dict.keys(parts)[i]
    elif dict.values(parts)[i]==2:
        group1_2[i]=dict.keys(parts)[i]
    else: 
        group1_2[i]=None
    i = i + 1 



G_1_2 = G_fb.subgraph(group1_2)
nx.draw_networkx(G_1_2, pos = spring_pos, cmap = plt.get_cmap("jet"), node_size = 15, with_labels = False)
print nx.info(G_1_2)





size = float(len(set(parts.values())))
#pos = spring_pos
count = 0.
for com in set(parts.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in parts.keys()
                                if parts[nodes] == com]
    nx.draw_networkx_nodes(G_fb, spring_pos, list_nodes, node_size = 15,
                                node_color = str(count / size))
nx.draw_networkx_edges(G_fb,spring_pos, alpha=0.5)
plt.show()




##### Dendo graph ######

dendo = community.generate_dendogram(G_fb)
for level in range(len(dendo) - 1) :
   print "partition at level", level, "is", community.partition_at_level(dendo, level)





##### induced graph ####

G=community.induced_graph(parts, G_fb)
#nx.draw_networkx(G, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 15, with_labels = False)
nx.draw_networkx(G)








