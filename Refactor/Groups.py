class Grups:
    #Constructor
    def __init__(self,letter,team1,team2,team3,team4) -> None:
        #Setting name of a group and teams within it
        self.letter = letter
        self.team1 = team1
        self.team2 = team2
        self.team3 = team3
        self.team4 = team4
        #List of matches in a group
        self.matches = [Match(self.team1,self.team2), atch(self.team3,self.team4),
         Match(self.team1,self.team3), Match(self.team4,self.team2),
         Match(self.team2,self.team3), Match(self.team4,self.team1)]
        for i in self.matches: match_data.append(i)
    def __str__(self) -> str:
        return f'{self.team1.name}\n{self.team2.name}\n{self.team3.name}\n{self.team4.name}\n'