import os
import sys
import random
from networkx import draw, Graph
from matplotlib import pyplot as plt

class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False
        
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.add_neighbor(neighbor)
        
    def __repr__(self):
        return str(self.neighbors)

class MyGraph:
    def __init__(self):
        self.vertices = {}
        self.vertices_number = 0
        self.generate_graph()
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

            
    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors
            
    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            vertex_from.add_neighbor(vertex_to)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors
                
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0],edge[1])

    def generate_edges(self, vertice, vertices):
        edges_number = random.randint(0, int(self.vertices_number/3))
        edges = []

        for _ in range(edges_number):
            index = random.randint(0, self.vertices_number - 1)
            if(vertices.index(vertice) == index):
                pass
            else:
                edge = [vertice, vertices[index]]
                edges.append(edge)        

        self.add_edges(edges)

    def generate_graph(self):
        self.vertices_number = random.randint(10, 20)
        print("quantidade de nos: " + str(self.vertices_number))
        vertices = [Vertex(str(vertice)) for vertice in range(self.vertices_number)]

        self.add_vertices(vertices)

        for vertice in vertices:
            self.generate_edges(vertice, vertices)

    def edges_tuples(self):
        keys = list(self.vertices.keys())
        keys_visited = []
        edges = []

        for key in keys:
            keys_visited.append(key)
            for neighbor in self.vertices[key]:
                if neighbor not in keys_visited:
                    edges.append((key, neighbor))

        return edges
    
    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]  
        else:
            return dict()
             
                        
def graph(g):
    """ Function to print a graph as adjacency list. """
    return str(g.adjacencyList()) + '\n'

def plot_graph(g):
    s = Graph()
    s.add_edges_from(g.edges_tuples())
    draw(s, with_labels=True)
    plt.savefig('grafo.png')

def nodes_to_path(g):
    pass

def smaller_path(g, node_from, node_to):
    pass

if __name__ == '__main__':

    points = 0

    print(  
            """
            \nOlá! Seja bem-vindo(a) ao jogo dos caminhos.\n
            \nVocê deve tentar acertar qual o menor caminho de um nó a outro do grafo pela maior quantidade de vezes consecutivas.\n
            """
        )

    os.system("read -p '\nPressione Enter para começar o jogo.' var")

    while True:      
        g = MyGraph()
        plot_graph(g)
        
        os.system("clear")

        node_from, node_to = nodes_to_path(g)

        print("Abra a figura 'grafo.png' gerada e indique o menor caminho do nó " + node_from.name + " ao nó " node_to.name + ".\n")
        print(
                """
                Ex: Sejam X e Y os nós de origem e destino. A, B e C nós que fazem a ligação entre X e Y.\n 
                Se você acreditar o menor caminho para se chegar de X até Y é passando por A, B e C, o caminho que deve ser indicado é: X-A-B-C-Y\n"
                """
            )
        
        path = input("\nIndique o caminho(" + node_from.name + ", " + node_to.name + ": ")

        if(path == smaller_path(g, node_from, node_to)):
            points += 1
            print("\nAcertou! Você tem " + str(points) + " pontos.\n")
        else:
            print("\nQue pena, você errou!\n")

        option = input("\n\nContinuar? (S/N): ")
        
        if(option == 'N')
            sys.exit()

