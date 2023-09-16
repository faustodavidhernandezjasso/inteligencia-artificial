class Graph:

    def __init__(self, graph_dictionary: dict) -> None:
        self.__graph_dictionary = graph_dictionary
        self.link_vertices()

    @property
    def graph_dictionary(self):
        return self.__graph_dictionary

    def link_vertices(self):
        for vertice in list(self.__graph_dictionary.keys()):
            for (neighbor, distance) in self.__graph_dictionary[vertice].items():
                self.__graph_dictionary.setdefault(neighbor, {})[vertice] = distance

    def get_distance(self, a, b):
        if not(a in self.__graph_dictionary) or not (b in self.__graph_dictionary):
            raise Exception("Non exists one of the keys or both.")
        return self.__graph_dictionary.get(a).get(b)