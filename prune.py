from gfa import GFA


def prune_main(args):
    res = Prune(args.gfa, args.kmer_length, args.edge_max).calculate_complexity()
    print(res)


class Prune(GFA):
    def __init__(self, gfafile, kmer_len, edge_max):
        super().__init__(gfafile)
        self.kmer_len = kmer_len
        self.edge_max = edge_max

    def calculate_complexity(self):
        return self.find_edges_to_prune()

    def find_edges_to_prune(self):
        print(self.gfafile, self.kmer_len, self.edge_max)
        print('Hello, World!')
        return 1

