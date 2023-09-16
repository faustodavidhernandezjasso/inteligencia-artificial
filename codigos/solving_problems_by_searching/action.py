class Action:

    def __init__(self, name_of_action) -> None:
        self.__name_of_action = name_of_action

    @property
    def name_of_action(self):
        return self.__name_of_action
    
    def __str__(self) -> str:
        return "Action: " + self.__name_of_action
    
    def __eq__(self, __value: object) -> bool:
        if (type(self) != __value):
            return False
        return self.__name_of_action == __value.__name_of_action
    
    def __hash__(self) -> int:
        return hash(self.__name_of_action)