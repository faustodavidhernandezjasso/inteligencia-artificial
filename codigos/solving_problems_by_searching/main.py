from search_problem import SearchProblem
from node import Node
from algorithms import Algorithms

def solution(node: Node):
    solution = []
    while (node != None):
        solution.append(node)
        node = node.parent
    return solution

def print_solution(solution: list):
    for node in reversed(solution):
        print(node)
        

if __name__ == '__main__':
    problem = SearchProblem()
    alg = Algorithms()
    node = alg.breadth_first_search(problem)
    print("BFS: ")
    print_solution(solution(node))
    node = alg.depth_first_search(problem)
    print("DFS: ")
    print_solution(solution(node))
    node = alg.a_star(problem)
    print("A*: ")
    print_solution(solution(node))