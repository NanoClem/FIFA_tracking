
var json = require('C:/Users/Boule/Downloads/chart_dataset.json');


function getChartBarPresence(data, minLength, maxLength){

    var lengthField = maxLength - minLength;
    var parts = divideField(lengthField, minLength, maxLength);
    var zones = createModelData();
    var totalCount = 0

    data.forEach(frame => {
        frame['records'].forEach(record => {
            totalCount++;
            var zone = locateZone(record['position'], parts);
            if (zone == 0){
                zones[0]["team" + record["team_id"]]["count"] += 1;
            }
            if (zone == 1){
                zones[1]["team" + record["team_id"]]["count"] += 1;
            }
            if (zone == 2){
                zones[2]["team" + record["team_id"]]["count"] += 1;
            }
        });
    });
    zones.forEach(zone => {
        zone["team1"]["perc"] = Math.round(zone["team1"]["count"] / totalCount * 100);
        zone["team2"]["perc"] = Math.round(zone["team2"]["count"] / totalCount * 100);
    });

    return zones;
};


function divideField(lengthField, minLength, maxLength){
    var div = Math.round(lengthField/3);
    var first_tierce = div + minLength;
    var second_tierce = div * 2 + minLength;
    return [minLength, first_tierce, second_tierce, maxLength];
}

function locateZone(position, parts, team, zones){
    var x = position["x"];
    var zone = NaN;
    if( x < parts[1])
        zone = 0;
    else if( x >= parts[1] && x < parts[2])
        zone = 1;
    else 
        zone = 2;
    return zone
    
}


function createModelData(){
    var zones = []
    for (let i = 0; i < 3; i++) {
        var zone = {
            "zone": i,
            "team1": {
                "count": 0,
                "perc": 0,
            },
            "team2": {
                "count": 0,
                "perc": 0,
            }
        }  
        zones.push(zone)
    }
    return zones
}

getChartBarPresence(json, 12, 50, 0, 39)

