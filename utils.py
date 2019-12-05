# GET vertices, edges for Hamiltonian path
def graph_hamiltonian(reads, k):
	k = 3
	reads = "GACCGCACGGCGACGAGAB"
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

	print(vertices)
	print(edges)
	return vertices, edges


# Get vertices and edges for euler path
def graph_euler(reads, k):
	k = 5
	reads = "GACCGCACGGCGACGAGAB"
	kmers = set([reads[i:i+k] for i in range(len(reads)-k+1)])
	nodes = sorted(set([kmer[:k-1] for kmer in kmers] + [kmer[1:k] for kmer in kmers]))

	print(kmers)

	vertices = {}
	edges = []
	for i,node in enumerate(nodes):
		vertices[node] = i


	for kmer in kmers:
	    e = [vertices[kmer[:k-1]],vertices[kmer[1:k]]]
	    edges.append(e)

	print(vertices)
	print(edges)

	return vertices, edges
