import time
from functools import partial
from informed_search import *
import math

class RomaniaMap:
    ARAD = "Arad"
    BUCHAREST = "Bucharest"
    CRAIOVA = "Craiova"
    DOBRETA = "Dobreta"
    EFORIE = "Eforie"
    FAGARAS = "Fagaras"
    GIURGIU = "Giurgiu"
    HIRSOVA = "Hirsova"
    IASI = "Iasi"
    LUGOJ = "Lugoj"
    MEHADIA = "Mehadia"
    NEAMT = "Neamt"
    ORADEA = "Oradea"
    PITESTI = "Pitesti"
    RIMNICU_VILCEA = "Riminicu Vilcea"
    SIBIU = "Sibiu"
    TIMISOARA = "Timisoara"
    URZICENI = "Urziceni"
    VASLUI = "Vaslui"
    ZERIND = "Zerind"

    positions = {
        ARAD: (46.166667, 21.316667),
        BUCHAREST: (44.4267674, 26.1025384),
        CRAIOVA: (44.333333, 23.816667000000052),
        DOBRETA: (44.636923, 22.659734),
        EFORIE: (44.058422, 28.633607),
        FAGARAS: (45.8416403, 24.9730954),
        GIURGIU: (43.903708, 25.969926),
        HIRSOVA: (44.6893481, 27.945655200000033),
        IASI: (47.156944, 27.590278000000012),
        LUGOJ: (45.6909898, 21.9034608),
        MEHADIA: (44.904114, 22.364516),
        NEAMT: (46.975869, 26.381876),
        ORADEA: (47.0465, 21.918944),
        PITESTI: (44.860556, 24.867778000000044),
        RIMNICU_VILCEA: (45.099675, 24.369318),
        SIBIU: (45.792784, 24.152068999999983),
        TIMISOARA: (45.759722, 21.23),
        URZICENI: (44.7165317, 26.641121),
        VASLUI: (46.640692, 27.727647),
        ZERIND: (46.622511, 21.517419)
    }

    map = {
        ARAD: [(ZERIND, 75), (TIMISOARA, 118), (SIBIU, 140)],
        BUCHAREST: [(URZICENI, 85), (GIURGIU, 90), (PITESTI, 101), (FAGARAS, 211)],
        CRAIOVA: [(DOBRETA, 120), (PITESTI, 138), (RIMNICU_VILCEA, 146)],
        DOBRETA: [(MEHADIA, 75), (CRAIOVA, 120)],
        EFORIE: [(HIRSOVA, 86)],
        FAGARAS: [(SIBIU, 99), (BUCHAREST, 211)],
        GIURGIU: [(BUCHAREST, 90)],
        HIRSOVA: [(EFORIE, 86), (URZICENI, 98)],
        IASI: [(NEAMT, 87), (VASLUI, 142)],
        LUGOJ: [(MEHADIA, 70), (TIMISOARA, 111)],
        MEHADIA: [(LUGOJ, 70), (DOBRETA, 75)],
        NEAMT: [(IASI, 87)],
        ORADEA: [(ZERIND, 71), (SIBIU, 151)],
        PITESTI: [(RIMNICU_VILCEA, 97), (BUCHAREST, 101), (CRAIOVA, 138)],
        RIMNICU_VILCEA: [(SIBIU, 80), (PITESTI, 97), (CRAIOVA, 146)],
        SIBIU: [(RIMNICU_VILCEA, 80), (FAGARAS, 99), (ARAD, 140), (ORADEA, 151)],
        TIMISOARA: [(LUGOJ, 111), (ARAD, 118)],
        URZICENI: [(BUCHAREST, 85), (HIRSOVA, 98), (VASLUI, 142)],
        VASLUI: [(IASI, 92), (URZICENI, 142)],
        ZERIND: [(ORADEA, 71), (ARAD, 75)]
    }

    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        return self.map[state]

    def result(self, state, action):
        return action[0]

    def step_cost(self, state, action):
        return action[1]

    def heuristic_cost(self, state, action):
        lat1, lon1 = self.positions[action[0]]
        lat2, lon2 = self.positions[self.goal]
        radius = 6371
        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
        return d


def raw_exec_time(problem):
    num_iter = 10000
    mean_time = 0
    for i in range(num_iter):
        start_time = time.clock()
        a_star_agent(problem)
        mean_time += (time.clock() - start_time)/num_iter    
    print("A*: " + format(mean_time, '.5f') + " seconds")

    mean_time = 0
    for i in range(num_iter):
        start_time = time.clock()
        greedy_best_first_agent(problem)
        mean_time += (time.clock() - start_time)/num_iter
    print("GBF: " + format(mean_time, '.5f') + " seconds")


if __name__ == '__main__':
    #loop
    #problem = RomaniaMap(RomaniaMap.IASI, RomaniaMap.ARAD)
    
    problem = RomaniaMap(RomaniaMap.ARAD, RomaniaMap.BUCHAREST)
    
    raw_exec_time(problem)
    
    solution = []
    '''
    a_star_agent(problem, lambda x: solution.append(x))
    print("A*: ", solution)
    solution = []
    '''
    greedy_best_first_agent(problem, lambda x: solution.append(x))
    print("GBF: ", solution)