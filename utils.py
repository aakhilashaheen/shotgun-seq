# Read the subsampled data and convert them into graphs
# with k-mers of length k
def process_samples(file, k):
    vertices = {}
    edges = []
    with open(file) as input:
        for line in input:
            line = line.strip()
            vertices, edges = graph_euler(line, k)

    return vertices, edges



# GET vertices, edges for Hamiltonian path
def graph_hamiltonian(reads, k):
    kmers = set([reads[i:i+k] for i in range(len(reads)-k+1)])
    nodes = kmers
    vertices = {}

    for i,node in enumerate(nodes):
        vertices[node] = i

    edges = []

    for s in nodes:
        for d in nodes:
            if (s[1:k] == d[0:k-1]):
                e = [vertices[s], vertices[d]]
                edges.append(e)

    return vertices, edges


# Get vertices and edges for euler path
def graph_euler(reads, k):
    kmers = set([reads[i:i+k] for i in range(len(reads)-k+1)])
    nodes = sorted(set([kmer[:k-1] for kmer in kmers] + [kmer[1:k] for kmer in kmers]))

    #print(kmers)

    vertices = {}
    edges = []
    for i,node in enumerate(nodes):
        vertices[node] = i


    for kmer in kmers:
        e = [vertices[kmer[:k-1]],vertices[kmer[1:k]]]
        edges.append(e)

    return vertices, edges
