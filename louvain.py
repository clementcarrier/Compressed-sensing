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
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'r'
#plt.rc('lines', linewidth=2, color='r')

G_fb = nx.read_edgelist("facebook.txt", create_using = nx.Graph(), nodetype = int)
print nx.info(G_fb)

#Create network layout for visualizations
spring_pos = nx.spring_layout(G_fb)

plt.axis("off")
nx.draw_networkx(G_fb, pos = spring_pos, with_labels = False, node_size = 15)


############### Louvain algo ###########
import community 
parts = community.best_partition(G)
values = [parts.get(node) for node in G.nodes()]

## Calculate the modularity ##
community.modularity(parts, G)

plt.axis("off")
nx.draw_networkx(G, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 15, with_labels = False)
nx.draw_networkx(G, pos = spring_pos, cmap = get_cmap(m), node_color = values, node_size = 15, with_labels = False)
#plt.savefig(graph, format='png')





#### Pour ploter trois communautes pour les gros graphs (typiquement Facebook) #####

group3= [None] * 4039
values3= [None] * 4039
i = 0
while i in G.nodes():
    if dict.values(parts)[i]==1:
        group3[i]=dict.keys(parts)[i]
        values3[i]=dict.values(parts)[i]
    elif dict.values(parts)[i]==2:
        group3[i]=dict.keys(parts)[i]
        values3[i]=dict.values(parts)[i]
    elif dict.values(parts)[i]==5:
        group3[i]=dict.keys(parts)[i]
        values3[i]=dict.values(parts)[i]
    else: 
        group3[i]=None
        values3[i]=None
    i = i + 1 




G_3 = G.subgraph(group3)
values3 = [x for x in values3 if x != None]
spring_pos_3 = nx.spring_layout(G_3)

nx.draw_networkx(G_3, pos = spring_pos_3, cmap = plt.get_cmap("jet"), width=0.8 ,vmin=1, vmax=6 ,node_color = values3, node_size = 10, with_labels = False)
print nx.info(G_3)










