import sys
sys.path.append("src")

from mentorCB import *

# types of stream
science = Stream("science")
arts = Stream("Arts")
commerce = Stream("Commerce")

# types of degree
bTech = Degree("Bachelor of Technology", "4 years", Difficulty.Medium)
mTech = Degree("Master of Technology", "2 Years", Difficulty.Tough)
bArch = Degree("Bachelor of Architecture", "5 Years", Difficulty.Medium)
mBBS = Degree("Bachelor of Medicine, Bachelor of Surgery", "5.5 Years", Difficulty.Tough)
bDS = Degree("Bachelor of Dental Surgery", "5 Years", Difficulty.Medium)
mS = Degree("Master of Surgery", "3 Years", Difficulty.Tough)
mD = Degree("Doctor of Medicine", "3 Years", Difficulty.Tough)
bVSC = Degree("Bachelor of Veterinary Science", "5 Years", Difficulty.Tough)
bSC = Degree("Bachelor of Sciecne", "3 Years", Difficulty.Medium)
mSC = Degree("Mster of Science", "2 Years", Difficulty.Medium)
pHd = Degree("Doctor of Philosophy", "3-6 Years", Difficulty.Tough)
nDA = Degree("National Defence Academy", "3 Years", Difficulty.Tough)
bA = Degree("Bachelor of Arts", "3 Years", Difficulty.Medium)
mA = Degree("Master of Arts", "2 Years", Difficulty.Medium)
bDes = Degree("Bachelor of Design", "3 Years", Difficulty.Medium)
mDes = Degree("Master of Design", "2 Years", Difficulty.Medium)
bHM = Degree("Bachelor of Hotel Management", "3 Years", Difficulty.Medium)
bFA = Degree("Bachelor of Fine Arts", "3 Years", Difficulty.Medium)
lLB = Degree("Bachelor of Legislative Law", "3 Years", Difficulty.Medium)
bCom = Degree("Bachelor of Commerce", "3 Years", Difficulty.Medium)
bBA = Degree("Bachelor of Business Administration", "3 Years", Difficulty.Medium)
mBA = Degree("Master of Business Administration", "3 Years", Difficulty.Medium)
iCA = Degree("Institute of Chartered Accountants", "3 Years", Difficulty.Tough)
bEd = Degree("Bachelor of Education", "2 Years", Difficulty.Medium)
uPSC = Degree("Union Public Service Commision", "Exam Based", Difficulty.Tough)
sSC = Degree("Staff Selection Commission", "Exam Based", Difficulty.Medium)
anyD = Degree("Any Degree", "None", Difficulty.Medium)
iRDI = Degree("Insurance Regulatory and Development Authority of India","Exam Based", Difficulty.Medium )

# types of field
engineering = Field("Engineering", [science])
medical = Field("Medical", [science])
sciHonours = Field("Honours", [science])

artsHonours = Field("Honours", [arts])
fineArts = Field("Fine Arts", [arts])
law = Field("Law", [arts])

comHonors = Field("Honours", [commerce])

army = Field("Army", [science, arts, commerce])
goverment = Field("Goverment", [science, arts, commerce])
general = Field("General", [science, arts, commerce])

# types of career
comEngineer = Career("Computer Engineer", Demand.High, bTech, 6.4)
civEngineer = Career("Civil Engineer", Demand.Medium, bTech, 4.5)
mechEngineer = Career("Mechanical Engineer", Demand.Medium, bTech, 4.2)
chemEngineer = Career("Chemical Engineer", Demand.Medium, bTech, 4.2)
elecEngineer = Career("Elecitral Engineer", Demand.Medium, bTech, 5)
bioEngineer = Career("Biomedical Engineer", Demand.High, bTech, 4)
petroEngineer = Career("Petroleum Engineer", Demand.High, bTech, 8)
aeroEngineer = Career("Aerospace Engineer", Demand.High, bTech, 8.2)
nuclearEngineer = Career("Nuclear Engineer", Demand.High, mTech, 10)
roboticEngineer = Career("Robotic Engineer", Demand.Medium, bTech, 5)
rDEngineer = Career("R&D Engineer", Demand.High, mTech, 13)
genetics = Career("Geneticst", Demand.Medium, mTech, 8)
architecture = Career("Architecture", Demand.Medium, bArch, 5)
doctor = Career("Doctor", Demand.High, mBBS, 8)
dentist = Career("Dentist", Demand.Medium, bDS, 5)
surgeon = Career("Surgeon", Demand.High, mS, 12)
psychiatrist = Career("Psychiatrist", Demand.High, mD, 10)
veterinarian = Career("Veterinarian", Demand.Medium, bVSC, 6.2)
bioTech = Career("Biotechnologist", Demand.Medium, bSC, 5)
microBio = Career("Microbiologist", Demand.Medium, bSC, 3.4)
forensic = Career("Forensic", Demand.Medium, bSC, 5)
bioChem = Career("Biochemist", Demand.Medium, bSC, 3.8)
pharma = Career("Pharamicst", Demand.High, bSC, 4)
researchSci = Career("Research Scientist", Demand.High, pHd, 8)
foodTech = Career("Food Technologist", Demand.Medium, bSC, 4)
fightPilot = Career("Fighter Pilot", Demand.High, nDA, 17)
psychologist = Career("Psychologist", Demand.Medium, bSC, 5)
mHCouselor = Career("Mental Health Counselor", Demand.Medium, mSC, 6)
meteorologists = Career("Meteorologists", Demand.Medium, mSC, 4)
navOff = Career("Navy Officer", Demand.High, nDA, 7)
nurse = Career("Nurse", Demand.Medium, bSC, 4)
agriIns = Career("Agricultural Inspector", Demand.Medium, bSC, 4.5)
marBio = Career("Marine Biologist", Demand.Medium, mSC, 7)
oTT = Career("Operation Theatre Technologists", Demand.Medium, bSC, 3.6)
astronomer = Career("Astronomer", Demand.High, pHd, 10)
athmoRe = Career("Atmospheric Researchers", Demand.Medium, mSC, 6)
zoologist = Career("Zoologist", Demand.Medium, bSC, 4)
wildBio = Career("Wildlife Biologist", Demand.Medium, mSC, 6)
epidlogist = Career("Epidemiologist", Demand.Medium, mSC, 6)

lawyers = Career("Lawyer", Demand.High, lLB, 6)
fashionDes = Career("Fashion Designer", Demand.Medium, bDes, 3.8)
historian = Career("Historian", Demand.Medium, pHd, 8)
cartographer = Career("Cartographer", Demand.Medium, mA, 3)
geographer = Career("Geographer", Demand.Medium, mA, 3.6)
eventPlanner = Career("Event Planer", Demand.Medium, bHM, 5)
hotelManager = Career("Hotel Manager", Demand.Medium, bHM, 4)
rehCounsellor = Career("Rehabilitation Counsellor", Demand.Low, bA, 3)
socialWorker = Career("Social Worker", Demand.Medium, bA, 3)
journalist = Career("Journalist", Demand.Medium, bA, 4)
politicalSci = Career("Political Scientist", Demand.Medium, mA, 6)
fashionSty = Career("Fashion Stylist", Demand.Medium, bDes, 5)
marketingEx = Career("Marketing Executive", Demand.Medium, mA, 5)
companySec = Career("Company Secretary", Demand.Medium, lLB, 6)
travelAg = Career("Travel Agent", Demand.Medium, bA, 4)
yogaIns = Career("Yoga Instructor", Demand.Medium, bA, 4)
graphicDesigner = Career("Graphics Desingner", Demand.Medium, bA, 4)
geoScientist = Career("Geoscienctist",Demand.High, pHd, 14)
hydrologist = Career("Hydrologist", Demand.Medium, pHd, 5)
animator = Career("Animator", Demand.Medium, bFA, 5)
designManager = Career("Design Manager", Demand.Medium, mDes, 6)
cateringOfficer = Career("Catering Officer", Demand.Medium, bHM, 5)
fSManger = Career("Food and service Manager", Demand.Medium, bHM, 4.8)
interiorDesigner = Career("Interior Designer", Demand.Medium, bDes, 3)

buinessAnalyst = Career("Buiness Analyst", Demand.Medium, bCom, 4)
accountant = Career("Accountant", Demand.Medium, bCom, 6)
charteredAccountant = Career("Chatered Accountant", Demand.High, iCA, 10)
investmentBanker = Career("Investment Banker", Demand.High, bCom, 7)
costAndManagmentAcc = Career("Cost and Management Accountant", Demand.Medium, iCA, 5)
managementAcc = Career("Management Accountant", Demand.Medium, bCom, 4)
economist = Career("Economist", Demand.Medium, bCom, 5)
actuary = Career("Actuary", Demand.High, iCA, 8)
finalcialAnalyst = Career("Finalcial Analyst", Demand.Medium, bCom, 4)
insurecePro = Career("Insurece Professional", Demand.Medium,iRDI, 4)
banker = Career("Banker", Demand.Medium, bCom, 5)
finalcialPlanner =  Career("Finalcial Planner", Demand.Medium, bCom, 5)
publicRelationManger = Career("Public Relation Manager",Demand.Medium, bBA, 3)
supChainMang = Career("Supply Chain Manager", Demand.Medium, mBA, 6)
stockBroker = Career("Stock Broker", Demand.Medium, bBA, 5)


# types of questions

# database of degrees

# database of field
engineering.defineCareers([comEngineer, bioEngineer, civEngineer, aeroEngineer, chemEngineer, elecEngineer, mechEngineer,
petroEngineer, nuclearEngineer, roboticEngineer, rDEngineer, genetics, architecture])

medical.defineCareers([doctor, dentist, surgeon, psychiatrist, veterinarian, pharma, nurse, oTT])

sciHonours.defineCareers([bioTech, microBio, forensic, bioChem, researchSci, foodTech, psychologist, mHCouselor, 
meteorologists, agriIns, marBio, astronomer, athmoRe, zoologist, wildBio, epidlogist])

# test
for field in fields:
    print(field.getData("name"), "strem ->", field.getData("streams"))
    print("---------------------")
    for career in field.getData("careers"):
        print(career.getData("name"))
    print("---------------------")