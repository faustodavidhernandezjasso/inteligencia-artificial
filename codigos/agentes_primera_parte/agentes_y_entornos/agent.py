import random as r
from perception import Perception

class Agent:

    def __init__(self, n, m):
        self.__n = n
        self.__m = m
        self.__x = r.randint(0, m - 1)
        self.__y = r.randint(0, n - 1)
        self.__percept_sequence = []

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def percept(self, matrix):
        self.__percept_sequence.append(Perception(self.__y, self.__x, matrix[self.__y, self.__x]))

    def agent_function(self, matrix):
        if matrix[self.__y, self.__x] == 1: # Sí está sucio limpiamos
            matrix[self.__y, self.__x] = 0
        else: # Sí no está sucio nos movemos.
            self.make_movement(matrix)

    def make_movement(self, matrix):
        if self.__x > 0 and self.__x < self.__m - 1: # Entonces me puedo mover hacia la derecha o hacia la izquierda.
            if self.__y > 0 and self.__y < self.__n - 1: # Entonces me puedo mover hacia arriba o hacia abajo.
                self.take_decision(r.randint(0, 3))
            elif self.__y <= 0: # Entonces no me puedo mover hacia abajo.
                self.take_decision(r.randint(0, 2))
            else: # Entonces no me puedo mover hacia arriba.
                self.take_decision(r.choice([0, 1, 3]))
        elif self.__x <= 0: # No me puedo mover hacia la izquierda.
            if self.__y > 0 and self.__y < self.__n - 1: # Entonces me puedo mover hacia arriba o hacia abajo.
                self.take_decision(r.choice([0, 2, 3]))
            elif self.__y <= 0: # Entonces no me puedo mover hacia abajo.
                self.take_decision(r.choice([0, 2]))
            else: # Entonces no me puedo mover hacia arriba.
                self.take_decision(r.choice([0, 3]))
        else: # No me puedo mover hacia la derecha
            if self.__y > 0 and self.__y < self.__n - 1: # Entonces me puedo mover hacia arriba o hacia abajo.
                self.take_decision(r.choice([1, 2, 3]))
            elif self.__y <= 0: # Entonces no me puedo mover hacia abajo.
                self.take_decision(r.choice([1, 2]))
            else: # Entonces no me puedo mover hacia arriba.
                self.take_decision(r.choice([1, 3]))
            
    def take_decision(self, p):
        if p == 0: # Nos movemos hacia la derecha.
            self.__x += 1
        elif p == 1: # Nos movemos hacia la izquierda.
            self.__x -= 1
        elif p == 2: # Nos movemos hacia la arriba.
            self.__y += 1
        else: # Nos movemos hacia abajo
            self.__y -= 1

    def __str__(self):
        l = len(self.__percept_sequence)
        if (l == 0):
            return "[]"
        s = self.__percept_sequence[0].__str__()
        for i in range(1, l):
            s += ", "
            s += self.__percept_sequence[i].__str__()
            if i % 4 == 0:
                s += "\n"
        return s
