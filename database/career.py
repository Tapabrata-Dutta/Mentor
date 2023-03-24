import sys
sys.path.append("src")

from mentorCB import *

# types of stream
science = Stream("Science")
arts = Stream("Arts")
commerce = Stream("Commerce")
general = Stream("General")

# types of degree

# types of career 
computerEngineer = Career("Computer Engineer",Demand.High, "8 LPA")
civilEngineer = Career("Civil Engineer", Demand.Medium, "5 LPA")
mechanicalEngineer = Career("Mechanical Engineer", Demand.Low, "4 LPA")
electricalEngineer = Career("Electrical Engineer", Demand.Medium, "6 LPA")
chemicalEnginer = Career("Chemical Engineer", Demand.High, "5 LPA")
autoMobileEngineer = Career("Automobile Engineer", Demand.Low, "4 LPA")
biotechEngineer = Career("Biotechology Engnieer", Demand.Medium, "4 LPA")
miningEngineer = Career("Mining Engineer", Demand.High, "5 LPA")
aerospaceEngineer = Career("Aerospace Engineer", Demand.High, "7 LPA")

doctor = Career("Doctor", Demand.High, "8 LPA")
dentist = Career("Dentist", Demand.High, "6 LPA")
homeopath = Career("Homeopath Doctor", Demand.Low, "3.5 LPA")
ayurved = Career("Ayurvedic doctor", Demand.Medium, "5 LPA")
pharmacist = Career("Pharmacist", Demand.Medium, "2.4 LPA")
nurse = Career("Nurse", Demand.Medium, "2.4 LPA")
paramedic = Career("Paramedic", Demand.Medium, "1.6 LPA")

# types of questions



# database Roadmap


#database career


# database stream
science.addCareer(computerEngineer)
science.addCareer(civilEngineer)
science.addCareer(mechanicalEngineer)
science.addCareer(electricalEngineer)
science.addCareer(chemicalEnginer)
science.addCareer(autoMobileEngineer)
science.addCareer(biotechEngineer)
science.addCareer(miningEngineer)
science.addCareer(aerospaceEngineer)

science.addCareer(doctor)
science.addCareer(dentist)
science.addCareer(homeopath)
science.addCareer(ayurved)
science.addCareer(pharmacist)
science.addCareer(paramedic)


# test
for career in science.getData("careers"):
    print("Career =", career.getData("name"))
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