import networkx as nx
import matplotlib.pyplot as plt

#Create empty grapth
G = nx.DiGraph()

#Add nodes (people)
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
G.add_nodes_from(people)

#Add connections betwenn nodes
G.add_edge("Alice", "Bob", weight=4)
G.add_edge("Alice", "Charlie", weight=2)
G.add_edge("Alice", "David", weight=5)
G.add_edge("Bob", "David", weight=10)
G.add_edge("Charlie", "Eve", weight=3)
G.add_edge("David", "Eve", weight=6)
G.add_edge("David", "Charlie", weight=7)


#Visualize graph
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_color="black", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Social network")
plt.show()
