import random
Dictionary = []
PeopleStat1List = []
PeopleStat2List = []
PeopleStat3List = []
PeopleStat4List = []
File = open("dictionary.txt", "r")  
Data = File.read()  
Dictionary = Data.split("\n")  
File.close() 

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
    Stat1 = PeopleStat1List[Person]
    Stat2 = PeopleStat2List[Person]
    Stat3 = PeopleStat3List[Person]
    Stat4 = PeopleStat4List[Person]
    print('\nStat 1: ',Stat1,
          '\nStat 2: ',Stat2,
          '\nStat 3: ',Stat3,
          '\nStat 4: ',Stat4,
          '\nFav word: ',Dictionary[len(Dictionary)%(Stat1*Stat2*Stat3-Stat4)])
CheckPerson(int(input('What person would you like to check: '))-1)