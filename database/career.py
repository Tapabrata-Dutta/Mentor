import sys
sys.path.append("src")

from mentorCB import *

# types of stream
science = Stream("Science")
arts = Stream("Arts")
commerce = Stream("Commerce")
general = Stream("General")

# types of career
engineering = Career("Engineering", Education.HigherSecondary)
medical = Career("Medical", Education.HigherSecondary)

# database
science.addCareer(engineering)
science.addCareer(medical)

data = science.getData()
careers = data[2]

for i in range(0, len(careers)):
    print(careers[i].getData()[0])