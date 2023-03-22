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
civilEngineering = Degree("B.Tech in Civil Engineering.", "4 Years", Difficulty.Medium)

# types of career 
softwareEngineer = Career("Software Engineer", Education.HigherSecondary)
civilEngineer = Career("Civil Engineer", Education.HigherSecondary)

# types of questions



# database degree
computerScience.addRoadMap(["12th PCM", "State level Exam or National level Exam"])
informationTechnology.addRoadMap(["12th PCM", "State level Exam or National level Exam"])
civilEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])

#database career
softwareEngineer.addDegree(computerScience)
softwareEngineer.addDegree(informationTechnology)
civilEngineer.addDegree(civilEngineering)

# database stream
science.addCareer(softwareEngineer)
science.addCareer(civilEngineer)

# test
for career in science.getData("careers"):
    print("Career =", career.getData("name"))
    print("Minimum Education =", career.getData("minimumEducation").name)
    print("Degrees->")
    print(".........................")

    for degree in career.getData("degrees"):
        print("...")
        print(degree.getData("name"))
        print("Duration =", degree.getData("duration"))
        print("Difficulty =", degree.getData("difficulty").name)
        print("Road Map =", degree.getData("roadMap"))

    print(".........................")