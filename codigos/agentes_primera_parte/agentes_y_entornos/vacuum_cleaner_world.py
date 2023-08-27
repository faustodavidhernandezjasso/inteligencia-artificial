import time
from agent import Agent
from environment import Environment

class VacuumCleanerWorld:

    def __init__(self, i, j):
        self.__environment = Environment(i, j)
        self.__agent = Agent(i, j)
    
    def make_simulation(self):
        # Condiciones Iniciales
        self.print_data()
        while True:
            # Comenzamos a percibir
            self.__agent.percept(self.__environment.matrix)
            self.print_data()
            time.sleep(1.5)
            # Comenzamos a actuar
            self.__agent.agent_function(self.__environment.matrix)
            self.print_data()
            time.sleep(1.5)
    
    def print_data(self):
        print("Estado actual del entorno: ")
        print(self.__environment)
        print("Secuencia de percepciones del agente hasta el momento: ")
        print(self.__agent)
        print("Posición del agente: ")
        print("(" + str(self.__agent.y) + ", " + str(self.__agent.x) + ")")

if __name__ == '__main__':
    i = 5
    j = 5
    v = VacuumCleanerWorld(i, j)
    v.make_simulation()
