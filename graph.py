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
        with open(self.gfafile, 'r') as f:
            for line in f:
                itemlist = line.rstrip().split('\t')
                if itemlist[0] == 'H':
                    continue
                elif itemlist[0] == 'S':
                    self.nodes.append(Node(itemlist[1], itemlist[2]))
                elif itemlist[0] == 'L':
                    self.edges.append(
                        Edge(
                            itemlist[1],
                            itemlist[3],
                            True if itemlist[2] == '-' else False,
                            True if itemlist[4] == '-' else False,
                            int(itemlist[5].split('M')[0])  # TODO: parse CIGAR
                        )
                    )
                elif itemlist[0] == 'P':
                    pass


class Node:
    def __init__(self, node_id, sequence):
        self.name = node_id
        self.sequence = sequence
        self.id = int(node_id)


class Edge:
    def __init__(self, from_id, to_id, from_start=False, to_end=False, overlap=0):
        self.from_id = from_id
        self.to_id = to_id
        self.from_start = from_start
        self.to_end = to_end
        self.overlap = overlap


class Path:
    def __init__(self, name, node_csv, cigar_csv):
        self.name = name
        self.mapping = parse_mapping(node_csv, cigar_csv)
        self.is_circular = False
        self.len = 0

    def parse_mapping(self, node_csv, cigar_csv):
        mapping = []
        for i, tmp_node, tmp_cigar in enumerate(zip(node_csv.split(','), cigar_csv.split(',')), 1):
            node_id = int(tmp_node[:-1])
            is_reverse = True if tmp_node[-1] == '-' else False
            mapping.append(Mapping(node_id, is_reverse, i))
        return mapping


class Mapping:
    def __init__(self, node_id, is_reverse, seqid, rank):
        self.position = Position(node_id, is_reverse, seqid)
        self.edit = []  # TODO: parse cigar
        self.rank = rank


class Position:
    def __init__(self, node_id, is_reverse, seqid):
        self.node_id = node_id
        self.offset = node_id
        self.is_reverse = is_reverse
        self.name = seqid
