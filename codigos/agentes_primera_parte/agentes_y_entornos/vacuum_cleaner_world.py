import time
from agent import Agent
from environment import Environment
from perception import Perception

class VacuumCleanerWorld:

    def __init__(self):
        self.__environment = Environment(4, 4)
        self.__agent = Agent(4, 4)
    
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
    v = VacuumCleanerWorld()
    v.make_simulation()
