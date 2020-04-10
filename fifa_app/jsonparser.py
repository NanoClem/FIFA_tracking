import json


class jsonparser:

    def __init__(self):
        self.json = {
            "teams" : [],
            "positions" : []
        }
    
    def insertTeam(self, team1_name, team1_color, team2_name, team2_color):
        team1 = {
            "team1_id" : 1,
            "team1_name" : team1_name,
            "team2_color" : team1_color
        }
        team2 = {
            "team2_id" : 2,
            "team2_name" : team2_name,
            "team2_color" : team2_color
        }
        self.json["Team"].append([team1, team2])

    def 






js = jsonparser()

js.insertTeam("Liverpool", "Red", "Chelsea", "Blue")
print(js.json)

        