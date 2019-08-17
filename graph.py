class Graph:
    def __init__(self, gfafile):
        self.gfafile = gfafile
        self.nodes = []
        self.edges = []
        self.paths = []
        self.node_size = len(self.nodes)
        self.edge_size = len(self.edges)
        self.path_size = len(self.paths)
    
    def calculate_complexity(self):
        return self.edge_size

    def parse_gfafile(self):
        pass
