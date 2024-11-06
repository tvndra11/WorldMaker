import random
PeopleStat1List = []
PeopleStat2List = []
PeopleStat3List = []
PeopleStat4List = []
def StatMaker(Variance):
    Stat = 1
    for i in range(int(Variance)):
        Stat = Stat + random.randint(0,1)
    return(Stat)
def MakeNewPerson():
    PeopleStat1List.append(StatMaker(15))
    PeopleStat2List.append(StatMaker(15))
    PeopleStat3List.append(StatMaker(15))
    PeopleStat4List.append(StatMaker(15))
for i in range(int(input('amount to generate: '))):
    MakeNewPerson()
def CheckPerson(Person):
    print('\nStat 1:',PeopleStat1List[Person],
          '\nStat 2:',PeopleStat2List[Person],
          '\nStat 3:',PeopleStat3List[Person],
          '\nStat 4:',PeopleStat4List[Person])
CheckPerson(int(input('What person would you like to check: '))-1)