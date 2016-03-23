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

############### Algorithm "Leading eigenvector method" ###############
#remarque: j'ai appelé le graphe G, pour plus de généralité, si tu veux tester pour FB, renomme G_fb G (c'est plus simple que de tout changer)
m=G.number_of_edges()
A=nx.adjacency_matrix(G)
deg=G.degree(np.arange(0,len(G))) #vecteur des degrés des noeuds (il y a len(G) noeuds)
k=np.fromiter(iter(deg.values()), dtype=int) #sert à convertir l'objet deg qui est un dictionnaire en objet numpy.array
P=np.outer(k,k)/(2*m) #produit dyadique de k avec k (= k*k^T, k un vecteur col) et à diviser la matrice retournée par 2m
B=A-P #matrice de modularité

val, vect = scipy.linalg.eigh(B, eigvals=(len(B)-1,len(B)-1)) #recupère la plus grande eigenval et son eigenvect associé 

s_opt=np.array(vect.flatten()>0,dtype=int) #le vecteur s optimal vaut 1 qd la coordonnée de l'eigenvect est >0, 0 sinon.

############### Community detection ###########
import community 
parts = community.best_partition(G_fb)
values = [parts.get(node) for node in G_fb.nodes()]



plt.axis("off")
nx.draw_networkx(G_fb, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 15, with_labels = False)
nx.draw_networkx(G_fb, pos = spring_pos, cmap = get_cmap(m), node_color = values, node_size = 15, with_labels = False)
#plt.savefig(graph, format='png')


#dict.values(parts)[2]
#dict.keys(parts)

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


#### Deux communautes #####

group1_2= [None] * 4039
values1_2= [None] * 4039
i = 0
while i in G_fb.nodes():
    if dict.values(parts)[i]==1:
        group1_2[i]=dict.keys(parts)[i]
        values1_2[i]=dict.values(parts)[i]
    elif dict.values(parts)[i]==2:
        group1_2[i]=dict.keys(parts)[i]
        values1_2[i]=dict.values(parts)[i]
    else: 
        group1_2[i]=None
        values1_2[i]=None
    i = i + 1 

#import numpy as np
#group1_2[1] = np.asarray(group1_2)


G_1_2 = G_fb.subgraph(group1_2)
values1_2 = [x for x in values1_2 if x != None]
spring_pos_1_2 = nx.spring_layout(G_1_2)

nx.draw_networkx(G_1_2, pos = spring_pos_1_2, cmap = plt.get_cmap("jet"), width=0.8 ,vmin=0, vmax=6 ,node_color = values1_2, node_size = 10, with_labels = False)
print nx.info(G_1_2)



#### Trois communautes #####

group3= [None] * 4039
values3= [None] * 4039
i = 0
while i in G_fb.nodes():
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

#import numpy as np
#group1_2[1] = np.asarray(group1_2)


G_3 = G_fb.subgraph(group3)
values3 = [x for x in values3 if x != None]
spring_pos_3 = nx.spring_layout(G_3)

nx.draw_networkx(G_3, pos = spring_pos_3, cmap = plt.get_cmap("jet"), width=0.8 ,vmin=1, vmax=6 ,node_color = values3, node_size = 10, with_labels = False)
print nx.info(G_3)




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








