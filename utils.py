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

    # line = 'GACGGCGGCGCACGGCGCAA'
    # for i in range(len(line)-k+1):
    #     kmers_repeats.append(line[i:i+k])   

    return vertices, edges

# Calculates the in and out degrees of each vertex
def degrees(edges, vertices):
    inDegree = {}
    outDegree = {}

    # Set default in and out as 1 for all the vertices:
    for vert in vertices.values():
        inDegree[vert] = 1
        outDegree[vert] = 1


    for edge in edges:
        src = edge[0]
        dst = edge[1]
        if src in outDegree.keys():
            outDegree[src] = outDegree.get(src) + 1
        else:
            outDegree[src] = 1
        if dst in inDegree.keys():
            inDegree[dst] = inDegree.get(dst) + 1
        else:
            inDegree[dst] = 1
    return inDegree, outDegree

def verify(inDegree, outDegree, vertices):
    start = 0
    end = 0
    for vert in vertices.values():
        ins = inDegree.get(vert)
        outs = outDegree.get(vert)
        print(vert, ins, outs)
        if (ins == outs):
            continue
        elif (ins - outs == 1):
            end = vert
        elif (outs - ins == 1):
            start = vert
        else:
            start, end = -1, -1
            break
    if (start >= 0) and (end >= 0):
        print("Gooodddd")
        return start
    else:
        return -1


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

    print(vertices)
        
    # Adding the kmer as the edge for the graph between suffix and prefix nodes
    for kmer1 in kmers_repeats:
        start = kmer1[:k-1]
        end = kmer1[1:k]
        edges.append([vertices[start], vertices[end]])

    # Sanity check
    inDegree, outDegree = degrees(edges, vertices)
    print(verify(inDegree, outDegree, vertices))

    return vertices, edges