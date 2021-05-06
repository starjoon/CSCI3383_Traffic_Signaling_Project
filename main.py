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


# This placed all the car paths and streets in hashcode.in into dictionary/list
# eg) streets: 'a-e' --> Street(0, 4, 40) & cars: Car(4, 'a-e e-f f-d d-b')
with open('FILE_LOCATION') as f:
    lines = f.readlines()
duration, numNodes, numStreets, numCars, bonus = [
    int(x) for x in lines.pop(0).split()]

streets = {}
for _ in range(numStreets):
    line = lines.pop(0).split()
    start = int(line[0])
    end = int(line[1])
    street_name = line[2]
    length = int(line[-1])
    streets[street_name] = Street(start, end, length)

cars = []
for _ in range(numCars):
    line = lines.pop(0).split()
    pathLength = int(line[0])
    path = line[1:]
    cars.append(Car(pathLength, path))
