import utils 
def main():
	# Run the sample.py file to generate the random over lapping reads first into the test100.txt file 
	# sample100.fa is the smaller version of the chromosome fasta file with first 100 lines
	# Usage "python sample.py sample100.fa > test100.txt"
	# The default version has 50% coverage, 0.3 mutations per 1000 bases for generating the reads.
    # Read the original file and subsample n random reads using subsample.py
    vertices, edges = utils.process_samples("test100.txt", 20)
    print("------------EDGES-------------")
    
    #print(edges)
    print("-----------VETICES-------------")
    #print(vertices)

if __name__ == '__main__':
    main()
