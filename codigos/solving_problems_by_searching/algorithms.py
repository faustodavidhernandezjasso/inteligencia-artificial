from action import Action
from search_problem import SearchProblem
from node import Node
from queue import PriorityQueue

class Algorithms:

    def __init__(self) -> None:
        pass

    def expand(self, problem: SearchProblem, node: Node):
        state = node.state
        for action in problem.actions(state):
            s = problem.result(state, action)
            cost = node.path_cost + problem.graph.graph_dictionary.get(state).get(s)
            yield Node(s, node, cost)

    def breadth_first_search(self, problem: SearchProblem):
        node = Node(problem.initial_state, None, 0)
        if problem.goal_state == node.state:
            return node
        frontier = [node]
        reached = [problem.initial_state]
        while frontier:
            n = frontier.pop(0)
            for child in self.expand(problem, n):
                s = child.state
                if problem.goal_state == s:
                    return child
                if not(s in reached):
                    reached.append(s)
                    frontier.append(child)
        return "Failure"
    
    def depth_first_search(self, problem: SearchProblem):
        node = Node(problem.initial_state, None, 0)
        if problem.goal_state == node.state:
            return node
        frontier = [node]
        reached = [problem.initial_state]
        while frontier:
            n = frontier.pop()
            for child in self.expand(problem, n):
                s = child.state
                if problem.goal_state == s:
                    return child
                if not(s in reached):
                    reached.append(s)
                    frontier.append(child)
        return "Failure"
    
    def a_star(self, problem: SearchProblem):
        # This is h(n) in f(n) = g(n) + h(n)
        straight_line_heuristic = dict(Arad=366, Mehadia=241, Bucharest=0,
                                      Neamt=234, Craiova=160, Oradea=380,
                                      Drobeta=242, Pitesti=100, Eforie=161,
                                      Rimnicu=193, Fagaras=176, Sibiu=253,
                                      Giurgiu=77, Timisoara=329, Hirsova=151,
                                      Urziceni=80, Iasi=226, Vaslui=199,
                                      Lugoj=244, Zerind=374)
        node = Node(problem.initial_state, None, 0)
        frontier = PriorityQueue()
        frontier.put((straight_line_heuristic[node.state], node))
        reached = dict()
        reached[problem.initial_state] = node
        while frontier:
            n = frontier.get()
            if problem.goal_state == n[1].state:
                return n[1]
            for child in self.expand(problem, n[1]):
                s = child.state
                if not(s in reached) or (child.path_cost < reached[s].path_cost):
                    reached[s] = child
                    frontier.put((child.path_cost + straight_line_heuristic[s], child))
        return "Failure"
