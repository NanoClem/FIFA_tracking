
var json = require('../datasets/chart_dataset.json');


/**
 * 
 * @param {*} totalSize 
 * @param {*} minSize 
 * @param {*} maxSize 
 */
function divideField(totalSize, minSize, maxSize) {

    var div = Math.round(totalSize/3);
    var first_tierce = div + minSize;
    var second_tierce = div * 2 + minSize;

    return [minSize, first_tierce, second_tierce, maxSize];
}


/**
 * Compute the zone of the field in which a postion is
 * @param {*} position 
 * @param {*} parts 
 * @param {*} orientation 
 */
function locateZone(position, parts, orientation) {

    var pos = orientation == "vertical" ? position["x"]:position["y"];
    var zone = null;
    
    if( pos < parts[1])
        zone = 0;
    else if( pos >= parts[1] && pos < parts[2])
        zone = 1;
    else 
        zone = 2;

    return zone
}


/**
 * Compute the percentage of a value
 * @param {Number} value 
 * @param {Number} total 
 */
function getPercentage(value, total) {
    return Math.round(100 * value/total );
}


function exists(team, array) {

    if (array.length == 0)
        return false;

    for (let i = 0; i < array.length; i++) {
        if (array[i]['team'] == team)
            return true;
    }

    return false;
}


/**
 * Create a data model for zones computing
 */
function createModelData() {

    var ret = [];
    var zone = {};

    for(var i = 1; i<4; i++) {
        zone = {
            zone: i,
            values: []
        }
        ret.push(zone);
    }
     
    return ret;
}


/**
 * 
 * @param {JSON} data
 * @param {String} orientation 
 * @param {Number} min 
 * @param {Number} max 
 * 
 * @returns {JSON}
 */
function getPresence(data, orientation, min, max) {
    
    let interval = max - min;
    let parts = divideField(interval, min, max)
    let ret = createModelData();
    let totalCount = 0;

    // Find occurences
    data.forEach( frame => {
        totalCount += frame['records'].length;
        frame['records'].forEach( rec => {
            let zone = locateZone(rec['position'], parts, orientation);     // find the zone the position belongs to
            // first occurrence for this zone
            if (!exists(rec['team_id'], ret[zone]['values'])) {
                ret[zone]['values'].push({ 
                    team: rec['team_id'],
                    count: 1,
                    perc: 0
                });
            } else {
                ret[zone]['values'].forEach( val => {
                    if (val['team'] == rec['team_id']) {
                        val['count']++;
                    }
                });
            }
        });
    });

    // Compute percentage
    ret.forEach( zone => {
        zone['values'].forEach( team => {
            team['perc'] = getPercentage(team['count'], totalCount);
        });
    });

    return ret;
}


console.log(getPresence(json, 'vertical', 15, 20)[2]);

