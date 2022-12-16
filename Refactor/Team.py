#A class responsible for team creation and its statistics
class Team:
    #Constructor
    def __init__(self,name: str) -> None:
        self.name = name.center(40)
        self.table = [['MP', 'W', 'T', 'L', 'GS', 'GL', 'AS', 'P'], [0, 0, 0, 0, 0, 0, 0, 0]]
    #Method for data update
    def updatescore(self,list: list) -> None:
        self.table[1] = list
    #Print override
    def __str__(self) -> str:
        return f'{self.name}:\n\
        Matches played:     {self.table[1][0]}\n\
        Matches won:                  {self.table[1][1]}\n\
        Matches tied:                    {self.table[1][2]}\n\
        Matches lost:                {self.table[1][3]}\n\
        Goals scored:        {self.table[1][4]}\n\
        Goals lost:       {self.table[1][5]}\n\
        Aggregate scoreline:      {self.table[1][6]}\n\
        Points:                     {self.table[1][7]}\n'