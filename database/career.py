import sys
sys.path.append("src")

from mentorCB import *

# types of stream
science = Stream("Science")
arts = Stream("Arts")
commerce = Stream("Commerce")
general = Stream("General")

# types of degree
computerScience = Degree("B.Tech in Computer Science", "4 Years", Difficulty.Medium)
informationTechnology = Degree("B.Tech in Information Technology", "4 Years", Difficulty.Medium)

# types of career 
softwareEngineering = Career("Software Engineering", Education.HigherSecondary)

# types of questions


# database degree
computerScience.addRoadMap(["12th (Science)", "State Level Exam or JEE"])
informationTechnology.addRoadMap(["12th (Science)", "State Level Exam or JEE"])

#database career
softwareEngineering.addDegree(computerScience)
softwareEngineering.addDegree(informationTechnology)

# database stream
science.addCareer(softwareEngineering)

# test
for career in science.getData("careers"):
    print("Career =", career.getData("name"))
    print("Minimum Education =", career.getData("minimumEducation").name)
    print("Degrees->")
    print(".........................")

    for degree in career.getData("degrees"):
        print("...")
        print("Name =", degree.getData("name"))
        print("Duration =", degree.getData("duration"))
        print("Difficulty =", degree.getData("difficulty").name)
        print("Road Map =", degree.getData("roadMap"))

    print(".........................")