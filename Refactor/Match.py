#Class for match pairs - overall
class Match():
    #Each match has individual ID to keep track of the progress. 
    id = 0
    #Constructor
    def __init__(self,team1,team2) -> None:
        self.team1 = team1
        self.team2 = team2
        self.name = f'{team1.name} - {team2.name}'
        self.score = [0,0]
        self.status = False
        self.id = Match.id
        Match.id += 1
    #Score update method
    def updatescore(self,v1: int,v2: int) ->None:
        self.score = [v1,v2]
    #Print override - ID should not be displayed in final release
    def __str__(self) -> str:
        if self.status:
            return (f'{self.team1.name} {self.score[0]} - {self.score[1]} {self.team2.name}')
        else:
            return f'ID: {self.id} {self.team1.name} - - - {self.team2.name}'