from functools import partial

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
        i


def __a_star(problem):
    node = Node(state = problem.initial_state, path_cost = 0)
    frontier = [node]
    explored = []
    while True:
        if len(frontier) == 0:
            raise Exception('Failure')
        node = frontier.pop(0)
        if problem.goal_test(node.state):
            return __solution(node)
        explored.append(node.state)
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action, True)
            if not (child.state in explored and any(x for x in frontier if x.state == child.state)):
                frontier.append(child)
                frontier = sorted(frontier)
            frontier = [child if x.state == child.state and x.path_cost > child.path_cost else x for x in frontier]


def __greedy_best_first(problem):
   node = Node(state = problem.initial_state, path_cost = 0)
   frontier = [node]
   explored = []
   while True:
        if len(frontier) == 0:
            raise Exception('Failure')
        node = frontier.pop(0)
        if problem.goal_test(node.state):
            return __solution(node)
        explored.append(node.state)
        for action in problem.actions(node.state):
            child = __child_node(problem, node, action)
            if not (child.state in explored and any(x for x in frontier if x.state == child.state)):
                frontier.append(child)
                frontier = sorted(frontier)
            frontier = [child if x.state == child.state and x.path_cost > child.path_cost else x for x in frontier] 


def __child_node(problem, parent, action, a_star=False):
    new_state = problem.result(parent.state, action)
    new_path_cost = problem.heuristic_cost(parent.state, action)
    if a_star == True:
        new_path_cost += parent.path_cost + problem.step_cost(parent.state, action)
    return Node(new_state, parent, action, new_path_cost)


def __solution(node):
    sol = []
    while node.action != None:
        sol.insert(0, node.action)
        node = node.parent
    return sol


def __simple_problem_solving_agent(problem, search, callback):
    try:
        seq = search(problem)
        while len(seq) != 0:
            callback(seq.pop(0))
    except Exception as e:
        return


def a_star_agent(problem, callback = None):
    __simple_problem_solving_agent(problem, __a_star, callback)


def greedy_best_first_agent(problem, callback = None):
    __simple_problem_solving_agent(problem, __greedy_best_first, callback)
