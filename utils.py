# Read the subsampled data and convert them into graphs
# with k-mers of length k
def process_samples(file, k):
    vertices = {}
    edges = []
    kmers = set()
    kmers_repeats = []
    with open(file) as input:
        #Each line here is a random read
        for line in input:
            line = line.strip()

            # Finding all k-mers from that read and making a non-unique []
            for i in range(len(line)-k+1):
                kmers_repeats.append(line[i:i+k])
                
        vertices, edges = graph_euler(kmers_repeats, k)

    return vertices, edges


# Get vertices and edges for euler path
def graph_euler(kmers_repeats,k):
    #print(kmers_repeats)

    # Choosing all unique k-1 mers to be the nodes in the graph
    nodes = []
    for k1 in kmers_repeats:
        prefix = k1[:k-1]
        suffix = k1[1:k]

        nodes.append(prefix)
        nodes.append(suffix)
    nodes = sorted(set(nodes))

    vertices = {}
    edges = []


    # Numeric labels for nodes for easy graph traversal
    for i,node in enumerate(nodes):
        vertices[node] = i
        
    # Adding the kmer as the edge for the graph between suffix and prefix nodes
    for kmer1 in kmers_repeats:
        start = kmer1[:k-1]
        end = kmer1[1:k]
        edges.append([vertices[start], vertices[end]])

    return vertices, edges