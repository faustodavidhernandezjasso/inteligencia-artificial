from search_problem import SearchProblem
from action import Action
from node import Node
from algorithms import Algorithms
from graph import Graph

if __name__ == '__main__':
    problem = SearchProblem()
    alg = Algorithms()
    node = alg.breadth_first_search(problem)
    path = []
    while (node != None):
        path.append(node)
        node = node.parent
    for node in reversed(path):
        print(node)
