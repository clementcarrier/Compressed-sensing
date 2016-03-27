# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:52:46 2016

@author: carrierclement
"""

import matplotlib.pyplot as plt
import networkx as nx
filename = 'karate.gml'
G_karate=nx.read_gml(filename)

print(nx.info(G_karate))

#Create network layout for visualizations
spring_pos = nx.spring_layout(G_karate)

plt.axis("off")
nx.draw_networkx(G_karate, pos = spring_pos, with_labels = False, node_size = 80)



############### Community detection ###########
import community as com
parts = com.best_partition(G_karate)
values = [parts.get(node) for node in G_karate.nodes()]



plt.axis("off")
nx.draw_networkx(G_karate, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, font_size=20,node_size = 80, with_labels = False)

## Calculate the modularity ##
com.modularity(parts, G_karate)

## induced graph : each community is represented as one node ##
help(com)
G_induced=com.induced_graph(parts, G_karate)
plt.axis("off")
nx.draw_networkx(G_induced, cmap = plt.get_cmap("jet"),  font_size=20,node_size = 80, with_labels = False)



