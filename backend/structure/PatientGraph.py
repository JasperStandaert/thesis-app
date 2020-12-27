import networkx as nx
class PatientGraph:

    graph = nx.Graph()


    def __init__(self, nodes):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(nodes)
        
        for drug in nodes:
            for interaction in drug.interactions:
                if interaction.drugB in self.graph.nodes():
                    if not self.graph.has_edge(self.graph.nodes(drug), self.graph.nodes(interaction.drugB)):
                        self.graph.add_edge(self.graph.nodes(drug), self.graph.nodes(interaction.drugB))


