class Perception:

    def __init__(self, n, m, status):
        self.__n = n
        self.__m = m
        self.__status = status

    def __str__(self):
        str_status = ""
        if self.__status == 1:
            str_status = "Sucio"
        else:
            str_status = "Limpio"
        return "[" + "(" + str(self.__n) + ", " + str(self.__m) + ")" + ", " + str_status + "]"