from typing import Any


class Node:

    def __init__(self, state, parent, path_cost):
        self.__state = state
        self.__parent = parent
        self.__path_cost = path_cost

    @property
    def state(self):
        return self.__state
    
    @property
    def parent(self):
        return self.__parent
    
    @property
    def path_cost(self):
        return self.__path_cost
    
    def __str__(self):
        return self.__state
    
    def __call__(self, state, parent, path_cost):
        return Node(state, parent, path_cost)