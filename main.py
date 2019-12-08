import utils 
def main():
    # Read the original file and subsample n random reads using subsample.py
    vertices, edges = utils.process_samples("sample.txt", 5)
    print("------------EDGES-------------")
    
    print(edges)
    print("-----------VETICES-------------")
    print(vertices)

if __name__ == '__main__':
    main()
