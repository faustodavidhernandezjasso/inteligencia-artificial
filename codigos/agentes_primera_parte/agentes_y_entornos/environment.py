import numpy as np
import random as r

class Environment:

    def __init__(self, n, m):
        self.__n = n
        self.__m = m
        self.__matrix = np.zeros((n, m))
        self.__fill_randomly()

    @property
    def n(self):
        return self.__n
    
    @property
    def m(self):
        return self.__m
    
    @property
    def matrix(self):
        return self.__matrix
    
    def __fill_randomly(self):
        for i in range(self.__n):
            for j in range(self.__m):
                self.__matrix[i][j] = r.randint(0, 1)
    
    def __str__(self):
        return str(self.__matrix)