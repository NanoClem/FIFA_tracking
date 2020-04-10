import json
import random


x = {

  "Team":[ 
    {
      "id" : 1,
      "name" : "Liverpool",
      "color" : "Red"
      
    },
    {
      "id" : 2,
      "name" : "Chelsea",
      "color" : "Blue"
      
    }],

  "positions": [

  ]
}

for i in range(50):
    players = []
    for j in range(21):
        coordinates = (random.uniform(0, 100), random.uniform(0, 100))
        player = {
            "player_id_Team": j%2 + 1,
            "coordinates": {
                "x": coordinates[0],
                "y": coordinates[1]
                }
            }
        players.append(player)
    obj = {
        "timestamp" : i,
        "players" : players
    }
    x["positions"].append(obj)


with open('../data.json', 'w') as outfile:
    json.dump(x, outfile)