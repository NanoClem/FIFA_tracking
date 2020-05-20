
var json = require('C:/Users/Boule/Downloads/chart_dataset.json');


function getVerticalChartBarPresence(data, minLength, maxLength){
    var orientation = "vertical"
    var lengthField = maxLength - minLength;
    var parts = divideField(lengthField, minLength, maxLength);
    var zones = createModelData();
    var totalCount = 0

    data.forEach(frame => {
        frame['records'].forEach(record => {
            totalCount++;
            var zone = locateZone(record['position'], parts, orientation);
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
        console.log(zone)
    });

    return zones;
};


function getHorizontalChartBarPresence(data, minWidth, maxWidth){
    var orientation = "horizontal"
    var widthField = maxWidth - minWidth;
    var parts = divideField(widthField, minWidth, maxWidth);
    var zones = createModelData();
    var totalCount = 0

    data.forEach(frame => {
        frame['records'].forEach(record => {
            totalCount++;
            var zone = locateZone(record['position'], parts, orientation);
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
        console.log(zone)
    });

    return zones;
};


function divideField(totalSize, minSize, maxSize){
    var div = Math.round(totalSize/3);
    var first_tierce = div + minSize;
    var second_tierce = div * 2 + minSize;
    return [minSize, first_tierce, second_tierce, maxSize];
}

function locateZone(position, parts, orientation){
    var pos;
    if (orientation == "vertical")
        pos = position["x"];
    else
        pos = position["y"];

    var zone = NaN;
    if( pos < parts[1])
        zone = 0;
    else if( pos >= parts[1] && pos < parts[2])
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

getVerticalChartBarPresence(json, 12, 50)

getHorizontalChartBarPresence(json, 12, 50)

