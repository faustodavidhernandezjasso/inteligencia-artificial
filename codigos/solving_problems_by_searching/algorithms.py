from action import Action
from search_problem import SearchProblem
from node import Node
from graph import Graph

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
        while len(frontier) != 0:
            n = frontier.pop(0)
            for child in self.expand(problem, n):
                s = child.state
                if problem.goal_state == s:
                    return child
                if not(s in reached):
                    reached.append(s)
                    frontier.append(child)
        return "Failure"