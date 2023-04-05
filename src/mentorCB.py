from enum import Enum

class Stream: pass
class Field: pass
class Career: pass
class Question: pass
class Degree: pass

class Difficulty: pass
class Demand: pass

fields = []

class Stream:
    __name = str
    __likeable = float
    __questions = None

    def __init__(self, name:str) -> None:
        self.__name = name
        self.__likeable = 0.0
        self.__questions = []

    def addQuestion(self, question:Question) -> None:
        if(self.__questions.__contains__(question) == False): self.__questions.append(question)
        else: raise Exception("question {0} already exist in the {1}".format(question.getData("question"), self.__name))
    
    def getData(self, data:str) -> any:
        if(data == "name"): return self.__name
        elif(data == "likeable"): return self.__likeable
        elif(data == "questions"): return self.__questions
        else: raise Exception("data name = {0} not found in {1} Stream Class".format(data, self.__name))

class Field:
    __name = str
    __likeable = float
    __streams = None
    __careers = None
    __questions = None

    def __init__(self, name:str, streams:list) -> None:
        global fields
        self.__name = name
        self.__likeable = 0.0
        self.__streams = streams
        self.__careers = []
        self.__questions = []
        
        fields.append(self)
    
    def defineCareers(self, careers:list[Career]) -> None:
        if(len(self.__careers) == 0): self.__careers = careers
        else: raise Exception("careers are already exist in the {1}".format(self.__name))
    
    def defineQuestions(self, questions:list[Question]) -> None:
        if(len(self.__questions) == 0): self.__questions = questions
        else: raise Exception("questions are already exist in the {1}".format(self.__name))

    def getData(self, data:str):
        if(data == "name"): return self.__name
        elif(data == "likeable"): return self.__likeable
        elif(data == "streams"): return self.__streams
        elif(data == "careers"): return self.__careers
        elif(data == "questions"): return self.__questions
        else: raise Exception("data {0} is not found in {1}".format(data, self.__name))



class Career:
    __name = str
    __degree = Degree
    __likable = float
    __demand = Demand
    __annualSalary = float

    def __init__(self, name:str, demand:Demand, degree:Degree, annualSalary:float) -> None:
        self.__name = name
        self.__likable = 0.0
        self.__demand = demand
        self.__annualSalary = annualSalary
        self.__degree = degree
    
    def getData(self, data:str) -> any:
        if(data == "name"): return self.__name
        elif(data == "likable"): return self.__likable
        elif(data == "degree"): return self.__degree
        elif(data == "demand"): return self.__demand
        elif(data == "annualSalary"): return self.__annualSalary
        else: raise Exception("data name = {0} not found in {1} Career Class".format(data, self.__name))
    
class Question:
    __rating = int
    __question = str
    __effects = None

    def __init__(self, question:str) -> None:
        self.__question = question
        self.__effects = []
    
    def getData(self, data:str) -> any:
        if(data == "rating"): return self.__rating
        elif(data == "question"): return self.__question
        elif(data == "effects"): return self.__effects
        else: raise Exception("data name = {0} not found in Question = {1}".format(data, self.__question))

class Degree:
    __name = str
    __duration = str
    __difficulty = Difficulty

    def __init__(self, name:str, duration:str, difficulty:Difficulty) -> None:
        self.__name = name
        self.__duration = duration
        self.__difficulty = difficulty
        
    def getData(self, data:str) -> any:
        if(data == "name"): return self.__name
        elif(data == "duration"): return self.__duration
        elif(data == "difficulty"): return self.__difficulty
        else: raise Exception("data name = {0} not found in {1} Degree Class".format(data, self.__name))
        
        
class Difficulty(Enum):
    Easy = 1
    Medium = 2
    Tough = 3

class Demand(Enum):
    Low = 1
    Medium = 2
    High = 3