import networkx as nx
class PatientGraph:

    graph = nx.Graph()


    def __init__(self, nodes):
        self.graph = nx.Graph()
        graph.add_nodes_from(nodes)
        
        for drug in nodes:
            for interaction in drug.interactions:
                if interaction.drugB in graph.nodes():
                    graph.add_edge(graph.nodes(drug), graph.nodes(interaction.drugB))


