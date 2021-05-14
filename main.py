import math
import random
import matplotlib as plt


# stores information of each street
class Street:

    def __init__(self, startNode, endNode, length):
        self.attributes = {}
        self.attributes['start'] = startNode
        self.attributes['end'] = endNode
        self.attributes['length'] = length

    def __str__(self):
        return str(self.attributes)

    def set(self, key, value):
        self.attributes[key] = value

    def get(self, key):
        return self.attributes[key]


# stores information for each car and its path
class Car:
    def __init__(self, pathLength, path):
        self.attributes = {}
        self.attributes['pathLength'] = pathLength
        self.attributes['path'] = path

    def __str__(self):
        return str(self.attributes)

    def set(self, key, value):
        self.attributes[key] = value

    def get(self, key):
        return self.attributes[key]


# This places all car paths and streets from hashcode.in input file into appropriate data structures
# eg) streets: 'a-e' --> Street(0, 4, 40) & cars: Car(4, 'a-e e-f f-d d-b')
with open('/Users/starjoon/Desktop/hashcode.in') as f:
    lines = f.readlines()
duration, numNodes, numStreets, numCars, bonus = [
    int(x) for x in lines.pop(0).split()]

# We can see how many nodes and edges there are in the Directed Weighted Graph, along with the number of cars traveling
print("Number of nodes: ", numNodes)
print("Number of edges: ", numStreets)
print("Number of nodes: ", numCars)

# Line by line, we can consolidate every street (two nodes connected by an edge) into a dictionary with object-oriented programming
streets = {}
for _ in range(numStreets):
    line = lines.pop(0).split()
    start = int(line[0])
    end = int(line[1])
    street_name = line[2]
    length = int(line[-1])
    streets[street_name] = Street(start, end, length)

# Same thing can be done to consolidate every car
cars = []
for _ in range(numCars):
    line = lines.pop(0).split()
    pathLength = int(line[0])
    path = line[1:]
    cars.append(Car(pathLength, path))


# In order to find the shortest path for all pairs of nodes in the graph, we will be implementing the Floyd-Warshall algorithm
# We will be comparing all possible paths through the graph between each pair of vertices, which will run in O(|V|^3)
# Initialize a nxn table to keep track of shortest path between pairs, where n is the number of nodes/vertices
table = [[math.inf for i in range(numNodes)] for j in range(numNodes)]

# Zero value across the diagonal; zero distance to itself
for node in range(numNodes):
    table[node][node] = 0

# Assign distance values between pairs of nodes from the given input data
for street, attributes in streets.items():
    start_node = attributes.get('start')
    end_node = attributes.get('end')
    distance = attributes.get('length')
    tablee[start_node][end_node] = distance

# Floyd-Warshall Algorithm O(|V|^3)
for i in range(numNodes):
    for j in range(numNodes):
        for k in range(numNodes):
            if table[j][k] > table[j][i]+table[i][k]:
                table[j][k] == table[j][i]+table[i][k]


# Given that we have 8000 nodes with 63968 edges in the Directed Weighted Graph, our computers do not possess enough processing power to run the algorithm
# In order to compromise, we can run the algorithm with a smaller sample size (reduce the number of streets) OR construct a graph around the given car paths
