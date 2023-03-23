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
mechanicalEngineering = Degree("B.Tech in Mechanical Engineering", "4 Years", Difficulty.Medium)
electricalEngineering = Degree("B.Tech in Electrical Engineering.", "4 Years", Difficulty.Tough)
chemicalEnginering = Degree("B.Tech in Chemical Engineering", "4 Year", Difficulty.Medium)
autoMobileEngineering = Degree("B.Tech in Automobile Engineering", "4 Years", Difficulty.Easy)
biotechEngineering = Degree("Biotechlogy Enginereeing", "4 Years", Difficulty.Easy)
miningEngineering = Degree("Bechelor of Engineering in Mining Engineering", "4 Years", Difficulty.Medium)
aerospaceEngineering = Degree("Bechelor of Engineering in Aero Space Engineerin", "4 Years", Difficulty.Tough)

mbbs = Degree("Bechelor of Medice and Bechelor of Surgery", "5.5 Years", Difficulty.Tough)
bds  = Degree("Bechelor of Dental Surgery", "5 Years", Difficulty.Tough)
bhms = Degree("Bechelor of Homeopathic Medicine & Surgery", "5.5 Years", Difficulty.Medium)
bams = Degree("Bechelor of Ayurvedic Medicine & Surgery","5.5 Years", Difficulty.Medium)
bpharma = Degree("Bechelor of Pharmacy", "4 Years", Difficulty.Medium)
dpharma = Degree("Diploma of Pharmacy", "2 Years", Difficulty.Easy)
bscNursing = Degree("Bachelor of Science in Nursing", "4 Years", Difficulty.Easy)
paramedical = Degree("Paramedical course", "2 Years", Difficulty.Low)
physicsHonors = Degree("Bechelor of Science in Physics", Difficulty.Tough)


# types of career 
softwareEngineer = Career("Software Engineer",Demand.High, "10 LPA", Education.HigherSecondary)
civilEngineer = Career("Civil Engineer", Demand.Medium, "5 LPA", Education.HigherSecondary)
mechanicalEngineer = Career("Mechanical Engineer", Demand.Low, "4 LPA", Education.HigherSecondary)
electricalEngineer = Career("Electrical Engineer", Demand.Medium, "6 LPA", Education.HigherSecondary)
chemicalEnginer = Career("Chemical Engineer", Demand.High, "5 LPA", Education.HigherSecondary)
autoMobileEngineer = Career("Automobile Engineer", Demand.Low, "4 LPA", Education.HigherSecondary)
biotechEngineer = Career("Biotechology Engnieer", Demand.Medium, "4 LPA", Education.HigherSecondary)
miningEngineer = Career("Mining Engineer", Demand.High, "5 LPA", Education.HigherSecondary)
aerospaceEngineer = Career("Aero Space Engineer", Demand.High, "7 LPA", Education.HigherSecondary)

mBBS = Career("Doctor", Demand.High, "8 LPA", Education.HigherSecondary)
bDS = Career("Dentist", Demand.High, "6 LPA", Education.HigherSecondary)
bHMS = Career("Homeopaths", Demand.Low, "3.5 LPA", Education.HigherSecondary)
bAMS = Career("Ayurvedic doctor", Demand.Medium, "5 LPA", Education.HigherSecondary)
bPharma = Career("Pharmacist", Demand.Medium, "2.4 LPA", Education.HigherSecondary)
dPharma = Career("Pharmacist", Demand.Low, "1.6 LPA", Education.Secondary)
bSCNuring = Career("Nurse", Demand.Medium, "2.4 LPA", Education.HigherSecondary)
paraMedical = Career("Paramedic", Demand.Medium, "1.6 LPA", Education.HigherSecondary)



# types of questions



# database Roadmap
computerScience.addRoadMap(["12th PCM", "State level Exam or National level Exam"])
informationTechnology.addRoadMap(["12th PCM", "State level Exam or National level Exam"])
civilEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
mechanicalEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
electricalEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
chemicalEnginering.addRoadMap(["12th PCM", "State level or National level Exam"])
autoMobileEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
biotechEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
miningEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
aerospaceEngineering.addRoadMap(["12th PCM", "State level or National level Exam"])
mbbs.addRoadMap(["12th PCBM", "NEET exam"])
bds.addRoadMap(["12th PCBM", "NEET exam"])
bhms.addRoadMap(["12th PCBM", "HSC Exam"])
bams.addRoadMap(["12th PCBM", "NEET, KEAM, IPU CET, BVP CET etc."])
bpharma.addRoadMap(["12th PCMB" "NEET, BITSAT, MHT CET, WBJEE"])
dpharma.addRoadMap(["10th ", "JEXPO  GPAT, AU AIMEE etc"])
paramedical.addRoadMap(["12th PCB", "NEET exam"])

#database career
softwareEngineer.addDegree(computerScience)
softwareEngineer.addDegree(informationTechnology)
civilEngineer.addDegree(civilEngineering)
mechanicalEngineer.addDegree(mechanicalEngineering)
electricalEngineer.addDegree(electricalEngineering)
chemicalEnginer.addDegree(chemicalEnginering)
autoMobileEngineer.addDegree(autoMobileEngineering)
biotechEngineer.addDegree(biotechEngineering)
miningEngineer.addDegree(miningEngineering)
aerospaceEngineer.addDegree(aerospaceEngineering)

mBBS.addDegree(mbbs)
bDS.addDegree(bds)
bHMS.addDegree(bhms)
bAMS.addDegree(bams)
bPharma.addDegree(bpharma)
dPharma.addDegree(dpharma)
paraMedical.addDegree(paramedical)


# database stream
science.addCareer(softwareEngineer)
science.addCareer(civilEngineer)
science.addCareer(mechanicalEngineer)
science.addCareer(electricalEngineer)
science.addCareer(chemicalEnginer)
science.addCareer(autoMobileEngineer)
science.addCareer(biotechEngineer)
science.addCareer(miningEngineer)
science.addCareer(aerospaceEngineer)

science.addCareer(mBBS)
science.addCareer(bDS)
science.addCareer(bHMS)
science.addCareer(bAMS)
science.addCareer(bPharma)
science.addCareer(dPharma)
science.addCareer(paraMedical)


# test
for career in science.getData("careers"):
    print("Career =", career.getData("name"))
    print("Minimum Education =", career.getData("minimumEducation").name)
    print("Demand =", career.getData("demand").name)
    print("Annual Salary =", career.getData("annualSalary"))
    print("Degrees->")
    print(".........................")

    for degree in career.getData("degrees"):
        print("...")
        print(degree.getData("name"))
        print("Duration =", degree.getData("duration"))
        print("Difficulty =", degree.getData("difficulty").name)
        print("Road Map =", degree.getData("roadMap"))

    print(".........................")