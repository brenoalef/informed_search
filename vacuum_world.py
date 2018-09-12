import time
from informed_search import *

class VacuumWorld:
    LEFT = "Left"
    RIGHT = "Right"
    SUCK = "Suck"    

    actions_list = [LEFT, RIGHT, SUCK]

    def __init__(self, initial_state):
        self.initial_state = initial_state

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.actions_list

    def result(self, state, action):
        if action == self.SUCK:
            return (state[0], [x for x in state[1] if x != state[0]])
        elif action == self.LEFT:
            return (self.LEFT, state[1])
        else:
            return (self.RIGHT, state[1])

    def step_cost(self, state, action):
        return 1
    
    def heuristic_cost(self, state):
        return len(state[1])


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
    problem = VacuumWorld((VacuumWorld.LEFT, [VacuumWorld.LEFT, VacuumWorld.RIGHT]))
    
    raw_exec_time(problem)
    
    solution = []
    '''
    a_star_agent(problem, lambda x: solution.append(x))
    print("A*: ", solution)
    solution = []
    '''
    greedy_best_first_agent(problem, lambda x: solution.append(x))
    print("GBF: ", solution)
