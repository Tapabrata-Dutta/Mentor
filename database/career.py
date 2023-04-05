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
lLB = Degree("Bachelor of Legislative Law", "3 Years", Difficulty.Medium)
bCom = Degree("Bachelor of Commerce", "3 Years", Difficulty.Medium)
bBA = Degree("Bachelor of Business Administration", "3 Years", Difficulty.Medium)
mBA = Degree("Master of Business Administration", "3 Years", Difficulty.Medium)
iCA = Degree("Institute of Chartered Accountants", "3 Years", Difficulty.Tough)
bEd = Degree("Bachelor of Education", "2 Years", Difficulty.Medium)
uPSC = Degree("Union Public Service Commision", "Exam Based", Difficulty.Tough)
sSC = Degree("Staff Selection Commission", "Exam Based", Difficulty.Medium)
anyD = Degree("Any Degree", "None", Difficulty.Medium)
iRDI = Degree("Insurance Regulatory and Development Authority of India","Exam Based", Difficulty.Medium)
iBE = Degree("IB ACIO Exam", "Exam Based", Difficulty.Tough)
comPilot = Degree("Commercial Pilot", "200 hr", Difficulty.Medium)

# types of field
engineering = Field("Engineering", [science])
medical = Field("Medical", [science])
sciHonours = Field("Honours", [science])

artsHonours = Field("Honours", [arts])
law = Field("Law", [arts])

comHonors = Field("Honours", [commerce])

nationalSec = Field("National Security", [science, arts, commerce])
# goverment = Field("Goverment", [science, arts, commerce]) # will try to add later
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
gameDeveloper = Career("Game Developer", Demand.Medium, bSC, 4.8)
researchSci = Career("Research Scientist", Demand.High, pHd, 8)
foodTech = Career("Food Technologist", Demand.Medium, bSC, 4)
psychologist = Career("Psychologist", Demand.Medium, bSC, 5)
mHCouselor = Career("Mental Health Counselor", Demand.Medium, mSC, 6)
meteorologists = Career("Meteorologists", Demand.Medium, mSC, 4)
nurse = Career("Nurse", Demand.Medium, bSC, 4)
agriIns = Career("Agricultural Inspector", Demand.Medium, bSC, 4.5)
marBio = Career("Marine Biologist", Demand.Medium, mSC, 7)
oTT = Career("Operation Theatre Technologists", Demand.Medium, bSC, 3.6)
astronomer = Career("Astronomer", Demand.High, pHd, 10)
athmoRe = Career("Atmospheric Researchers", Demand.Medium, mSC, 6)
zoologist = Career("Zoologist", Demand.Medium, bSC, 4)
wildBio = Career("Wildlife Biologist", Demand.Medium, mSC, 6)
epidlogist = Career("Epidemiologist", Demand.Medium, mSC, 6)

lawyer = Career("Lawyer", Demand.High, lLB, 6)
corporateLawyer = Career("Corporate Lawyer", Demand.Medium, lLB, 7)
judge = Career("Judge", Demand.High, lLB, 12)
mediator = Career("Mediator", Demand.Medium, lLB, 6)
counsel = Career("Counsel", Demand.Medium, lLB, 6.2)
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
geoScientist = Career("Geoscienctist",Demand.High, pHd, 14)
hydrologist = Career("Hydrologist", Demand.Medium, pHd, 5)
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

teacher = Career("Teacher", Demand.Medium, bEd, 6)
professor = Career("Professor", Demand.High, pHd, 9)
contentCreator = Career("Content Creator", Demand.Medium, anyD, 4)
sportsPerson = Career("Sports Person", Demand.Medium, anyD, 4)
coach = Career("Coach", Demand.Medium, bEd, 5)
gamer = Career("Gamer", Demand.Low, anyD, 3)
graphicDesigner = Career("Graphics Desingner", Demand.Medium, anyD, 4)
animator = Career("Animator", Demand.Medium, anyD, 5)
airHostess = Career("Air Hostess", Demand.Medium, bBA, 6)
socialMediaMang = Career("Social Media Manager", Demand.Low, anyD, 3)
photographer = Career("Photographer", Demand.Medium, anyD, 4)
flimMaker = Career("Flim Maker", Demand.Medium, anyD, 4)
actor = Career("Actor", Demand.Medium, anyD, 4)
model = Career("Model", Demand.Medium, anyD, 4)
librarian = Career("Librarian", Demand.Medium, anyD, 6)
digitalMarketing = Career("Digital Marketing", Demand.Medium, anyD, 6)
commercialPilot = Career("Commercial Pilot", Demand.High,comPilot, 8)
aerobicInstructor = Career("Aerobic Instructor", Demand.Medium, anyD, 4)
chef = Career("Chef", Demand.Medium, bHM, 5)
dancer = Career("Dancer", Demand.Medium, anyD, 4)
painter = Career("Painter", Demand.Medium, anyD, 4)
singer = Career("Singer", Demand.Medium, anyD, 4)
videoEditor = Career("Video Editor", Demand.Medium, anyD, 4)

policeOff = Career("Police Officer", Demand.Medium, sSC, 5)
armyOff = Career("Army Officer", Demand.Medium, nDA, 5)
fightPilot = Career("Fighter Pilot", Demand.High, nDA, 17)
navOff = Career("Navy Officer", Demand.High, nDA, 7)
customOfficial = Career("Custom Official", Demand.Medium, sSC, 5)
incomeTaxOff = Career("Income Tax Officer", Demand.Medium, sSC, 6)
cbiOfficer = Career("Central Bureau of Investigation(CBI) Ofiicer", Demand.High, uPSC, 7)
cidOfficer = Career("Crime Investigation Department(CID) Officer", Demand.High, uPSC, 6)
iBOff = Career("Intelligence Bureau Officer", Demand.High, iBE, 6)
iPSOfficer = Career("Indian Police Service(IPS) Officer", Demand.High, uPSC, 12)
iASOfficer = Career("Indian Administrative Service(IAS) Officer", Demand.High, uPSC, 12)
iFSOfficer = Career("Indian Foreign Service(IFS) Officer", Demand.High, uPSC, 7.2)

# types of questions

# database of field
engineering.defineCareers([comEngineer, bioEngineer, civEngineer, aeroEngineer, chemEngineer, elecEngineer, mechEngineer,
petroEngineer, nuclearEngineer, roboticEngineer, rDEngineer, genetics, architecture])

medical.defineCareers([doctor, dentist, surgeon, psychiatrist, veterinarian, pharma, nurse, oTT])

sciHonours.defineCareers([bioTech, microBio, forensic, bioChem, researchSci, foodTech, psychologist, mHCouselor, 
meteorologists, agriIns, marBio, astronomer, athmoRe, zoologist, wildBio, epidlogist, gameDeveloper])

artsHonours.defineCareers([fashionDes, historian, cartographer, geographer, rehCounsellor, eventPlanner, hotelManager,
socialWorker, journalist, politicalSci, fashionSty, travelAg, yogaIns, geoScientist, hydrologist,
designManager, cateringOfficer, interiorDesigner])

comHonors.defineCareers([buinessAnalyst, accountant, charteredAccountant, investmentBanker, costAndManagmentAcc, 
managementAcc, economist, actuary, finalcialAnalyst, insurecePro, banker, finalcialPlanner, publicRelationManger,
supChainMang, stockBroker])

law.defineCareers([lawyer, corporateLawyer, judge, mediator, counsel, companySec])

nationalSec.defineCareers([policeOff, armyOff, fightPilot, navOff, incomeTaxOff, cbiOfficer, cidOfficer, iBOff,
iASOfficer, iPSOfficer, iFSOfficer, customOfficial])

general.defineCareers([teacher, professor, contentCreator, sportsPerson, coach, gamer, graphicDesigner, animator,
airHostess, socialMediaMang, photographer, flimMaker, actor, model, librarian, digitalMarketing, commercialPilot,
aerobicInstructor, chef, dancer, painter, singer, videoEditor])

# test
count = 0

for field in fields:
    print(field.getData("name"), "stream ->", field.getData("streams")[0].getData("name"))
    print("---------------------")
    for career in field.getData("careers"):
        print(career.getData("name"))
        count += 1
    print("---------------------")

print("total count =", count)