class BellmanFord:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.predecessor = [-1] * vertices

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def shortest_path(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        self.predecessor = [-1] * self.V

        # Relaxamento das arestas (V-1 vezes)
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    self.predecessor[v] = u

        # Verificação de ciclos negativos
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Ciclo negativo detectado!")
                return None

        return dist

    def get_path(self, src, dest):
        """Reconstrói o caminho de src até dest"""
        caminho = []
        atual = dest
        while atual != -1:
            caminho.append(atual)
            if atual == src:
                break
            atual = self.predecessor[atual]

        if caminho[-1] != src:
            return None  # não há caminho
        return list(reversed(caminho))


# Exemplo de uso
if __name__ == "__main__":
    bf = BellmanFord(5)
    bf.add_edge(0, 1, -1)
    bf.add_edge(0, 2, 4)
    bf.add_edge(1, 2, 3)
    bf.add_edge(1, 3, 2)
    bf.add_edge(1, 4, 2)
    bf.add_edge(3, 2, 5)
    bf.add_edge(3, 1, 1)
    bf.add_edge(4, 3, -3)

    dist = bf.shortest_path(0)
    if dist:
        print("Distâncias mínimas:", dist)
        print("Caminho até 3:", bf.get_path(0, 3))
