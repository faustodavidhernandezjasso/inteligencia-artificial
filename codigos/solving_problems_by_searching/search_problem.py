from graph import Graph
from action import Action

class SearchProblem:

    def __init__(self) -> None:
        self.__initial_state = "Oradea"
        self.__goal_state = "Hirsova"
        self.__graph = Graph(dict(
                            Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
                            Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
                            Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
                            Drobeta=dict(Mehadia=75),
                            Eforie=dict(Hirsova=86),
                            Fagaras=dict(Sibiu=99),
                            Hirsova=dict(Urziceni=98),
                            Iasi=dict(Vaslui=92, Neamt=87),
                            Lugoj=dict(Timisoara=111, Mehadia=70),
                            Oradea=dict(Zerind=71, Sibiu=151),
                            Pitesti=dict(Rimnicu=97),
                            Rimnicu=dict(Sibiu=80),
                            Urziceni=dict(Vaslui=142)))
        
    @property
    def initial_state(self):
        return self.__initial_state
    
    @property
    def goal_state(self):
        return self.__goal_state
    
    @property
    def graph(self):
        return self.__graph

    def actions(self, state):
        set_of_actions = set()
        for key in list(self.__graph.graph_dictionary.get(state).keys()):
            action = Action("To" + key)
            set_of_actions.add(action)
        return set_of_actions

    
    def result(self, state, action: Action):
        return action.name_of_action.removeprefix('To')
    
    def action_cost(self, state, new_state):
        return self.__graph.get_distance(state, new_state)
    

# if __name__ == '__main__':
#     problem = SearchProblem()
#     for action in problem.actions('Arad'):
#         print(problem.result('Arad', action))
#         print(action.name_of_action)