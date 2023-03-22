from enum import Enum


class Career:
    pass


class Stream:
    pass


class Question:
    pass


class Degree:
    pass


class Education:
    pass


class Difficulty:
    pass


class Stream:
    __name = str
    __likeable = float
    __careers = []

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__likeable = 0.0

    def addCareer(self, career: Career) -> None:
        self.__careers.append(career)
        career.changeStream(self)

    def getData(self, data: str) -> any:
        if (data == "name"):
            return self.__name
        elif (data == "likeable"):
            return self.__likeable
        elif (data == "careers"):
            return self.__careers
        else:
            raise Exception(
                "data name = {0} not found in {1} Stream Class".format(data, self.__name))


class Career:
    __name = str
    __stream = None
    __degrees = []
    __likable = float
    # __demand
    # __annualSalary
    __minimumEducation = Education

    def __init__(self, name: str, minEdu: Education) -> None:
        self.__name = name
        self.__likable = 0.0
        self.__minimumEducation = minEdu

    def addDegree(self, degree: Degree):
        self.__degrees.append(degree)

    def changeStream(self, stream: Stream):
        if (self.__stream != None):
            raise Exception("{0} already in {1} so it can't enter {2}".format(self.__name,
                                                                              self.__stream.getData("name"), stream.getData("name")))
        else:
            self.__stream = stream

    def getData(self, data: str) -> any:
        if (data == "name"):
            return self.__name
        elif (data == "stream"):
            return self.__stream
        elif (data == "degrees"):
            return self.__degrees
        elif (data == "likable"):
            return self.__likable
        elif (data == "minimumEducation"):
            return self.__minimumEducation
        else:
            raise Exception(
                "data name = {0} not found in {1} Career Class".format(data, self.__name))


class Question:
    __rating = int
    __question = str
    __careerEffect = []
    __streamEffect = []

    def __init__(self, question: str) -> None:
        self.__question = question

    def getData(self, data: str) -> any:
        if (data == "rating"):
            return self.__rating
        elif (data == "question"):
            return self.__question
        elif (data == "careerEffect"):
            return self.__careerEffect
        elif (data == "streamEffect"):
            return self.__streamEffect
        else:
            raise Exception("data name = {0} not found in Question = {1}".format(
                data, self.__question))


class Degree:
    __name = str
    __duration = str
    __difficulty = Difficulty
    __roadMap = []

    def __init__(self, name: str, duration: str, difficulty: Difficulty) -> None:
        self.__name = name
        self.__duration = duration
        self.__difficulty = difficulty

    def addRoadMap(self, steps: list[str]) -> None:
        if (len(self.__roadMap) > 0):
            raise Exception(
                "Road Map is already present in {0}".format(self.__name))
        else:
            self.__roadMap = steps

    def getData(self, data: str) -> any:
        if (data == "name"):
            return self.__name
        elif (data == "duration"):
            return self.__duration
        elif (data == "difficulty"):
            return self.__difficulty
        elif (data == "roadMap"):
            return self.__roadMap
        else:
            raise Exception(
                "data name = {0} not found in {1} Degree Class".format(data, self.__name))


class Education(Enum):
    Secondary = 1
    HigherSecondary = 2


class Difficulty(Enum):
    Easy = 1
    Medium = 2
    Tough = 3
