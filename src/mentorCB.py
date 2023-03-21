from enum import Enum

class Career:
    pass

class Stream:
    pass

class Question:
    pass

class Stream:
    __name = ""
    __likeable = 0.0
    __careers = []
    __question = []

    def __init__(self, name:str) -> None:
        self.__name = name
    
    def addCareer(self, career:Career) -> None:
        self.__careers.append(career)
    
    def getData(self) -> tuple():
        return (self.__name, self.__likeable, self.__careers, self.__question)

class Career:
    __name = ""
    __likable = 0.0
    __minEdu = Enum

    def __init__(self, name:str, minEdu:Enum) -> None:
        self.__name = name
        self.__minEdu = minEdu
    
    def getData(self) -> tuple():
        return (self.__name, self.__likable, self.__minEdu)

class Question:
    __rating = 0
    __question = ""

    def __init__(self, question:str) -> None:
        self.__question = question
    
    def getData(self) -> tuple():
        return (self.__rating, self.__question)

class Education(Enum):
    Secondary = 1
    HigherSecondary = 2
