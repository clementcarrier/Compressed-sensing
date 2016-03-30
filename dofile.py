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

############### Algorithm "Vector partitioning" ###############
#Attention cas particulier, 2 groupes, 2 valeurs propres.
p=2
val_p, vect_p = scipy.linalg.eigh(B, eigvals=(len(B)-p,len(B)-1)) #calcule les p leading eigenval et eigenvect
alpha=(1/(n-p))*np.sum(allval[:(len(allval)-p)]) #Détermination de alpha selon le paragraphe "D. Choice of \alpha" 
Z=np.tile(np.sqrt(val_p-alpha),n).reshape(p,n) #Matrice intermédiaire (pour construire la matrice des r_i) du type Z=[sqrt(beta-alpha]|..|sqrt(beta-alpha)] on répète n fois le même vecteur
r_mat=Z*vect_p.transpose() #Produit terme à terme de la mat inter avec les vecteurs propres (U dans l'équation (36) )
#début de l'algo
R=r_mat[:,0] #on met par défaut le premier individu dans le groupe 1
s=np.zeros(n) #on initialise le vecteurs des individus à 0,...,0
for iter in range(0,10):
    for i in range(0,n): # On passe en revue tous les noeuds
        if np.dot(R,r_mat[:,i])>0: #si le produit scalaire et positif ...
            if s[i]!=1:            #et que l'individu i n'est pas déjà présent dans le groupe 1
                R=R+r_mat[:,i]     #on augmente la matrice R de r_i
                x[i]=1             #et on ajoute l'individu i au vecteurs des individus du groupe 1
        else:                      #Si le produit scalaire est négatif ....
            if s[i]==1:            #et que l'individu était présent dans le groupe 1
                R=R-r_mat[:,i]     #on diminue la matrice R de r_i
                s[i]=0             #et on retire cet individu du vecteurs des individus du groupe 1

#En comparant s et s_opt, on voit que c'est à peu près similaire.










############### Louvain algo ###########
import community 
parts = community.best_partition(G_fb)
values = [parts.get(node) for node in G_fb.nodes()]

## Calculate the modularity ##
community.modularity(parts, G_fb)

plt.axis("off")
nx.draw_networkx(G_fb, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 15, with_labels = False)
nx.draw_networkx(G_fb, pos = spring_pos, cmap = get_cmap(m), node_color = values, node_size = 15, with_labels = False)
#plt.savefig(graph, format='png')





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








