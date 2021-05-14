import math
import random
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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
print("Number of cars: ", numCars)

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
    table[start_node][end_node] = distance

# Floyd-Warshall Algorithm O(|V|^3)
for i in range(numNodes):
    for j in range(numNodes):
        for k in range(numNodes):
            if table[j][k] > table[j][i]+table[i][k]:
                table[j][k] == table[j][i]+table[i][k]


# Given that we have 8000 nodes with 63968 edges in the Directed Weighted Graph, our computers do not possess enough processing power to run the algorithm
# In order to compromise, we can run the algorithm with a smaller sample size by constructing a graph around the given car paths

# Random sample 20 cars to start with a smaller sample size of nodes/edges for our new graph
# Since we will be using a different set of nodes/edges, we have to re-index our data before setting up the table

sampleNodes = set()
sampleEdges = set()

sampleCars = random.sample(cars, 20)
for car in sampleCars:
    for path in car.get('path'):
        start_end = path.split('-')
        if start_end[0] not in sampleNodes:
            sampleNodes.add(start_end[0])
        if start_end[1] not in sampleNodes:
            sampleNodes.add(start_end[1])
        if path not in sampleEdges:
            sampleEdges.add(path)

sampleNodes = sorted(list(sampleNodes))

indexMap = {}
mapCounter = 0
for node in sampleNodes:
    indexMap[node] = mapCounter
    mapCounter += 1

print(f"Number of nodes in reduced graph (20 cars): {len(sampleNodes)}")
print(f"Number of edges in reduced graph (20 cars): {len(sampleEdges)}")


# Now we can build a smaller table and run the Floy-Warshall Algorithm
sampleTable = [[math.inf for i in range(len(sampleNodes))]
               for j in range(len(sampleNodes))]

# Zero value across the diagonal; zero distance to itself
for node in range(len(sampleNodes)):
    sampleTable[node][node] = 0

# Assign distance values between pairs of nodes from the given input data
for i in range(len(sampleCars)):
    for j in range(len(sampleCars[i].get('path'))):
        car_ij = sampleCars[i].get('path')[j].split('-')
        sampleTable[indexMap[car_ij[0]]][indexMap[car_ij[1]]
                                         ] = streets[sampleCars[i].get('path')[j]].get('length')

# Floyd-Warshall Algorithm O(|V|^3)
for i in range(len(sampleNodes)):
    for j in range(len(sampleNodes)):
        for k in range(len(sampleNodes)):
            if sampleTable[j][k] > sampleTable[j][i]+sampleTable[i][k]:
                sampleTable[j][k] == sampleTable[j][i]+sampleTable[i][k]
