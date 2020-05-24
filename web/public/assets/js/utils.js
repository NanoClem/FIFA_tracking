/**
 * print format integer
 */
var formatAsInteger = d3.format(",");

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

    var pos = orientation == 'vertical' ? position['x']:position['y'];
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
 * Create a data model for zones
 * @param {String} orientation 
 */
function createDataModel(orientation) {

    var ret = [];
    var zone = {};
    
    // checking orientation
    if (orientation == 'vertical' || orientation == 'horizontal') {
        for(var i = 1; i<4; i++) {
            if (orientation == 'vertical')          // vertical zones
                zone = {zone: i, values: []};
            else if (orientation == 'horizontal')   // hoeizontal zones
                zone = {zone: i};
            ret.push(zone);
        }
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
function getVPresence(data, min, max) {
    
    let interval = max - min;
    let parts = divideField(interval, min, max);
    let orientation = 'vertical';
    let ret = createDataModel(orientation);
    let totalCount = 0;
    let zone;

    // count occurences
    data.forEach( frame => {
        totalCount += frame['records'].length;
        frame['records'].forEach( rec => {
            zone = locateZone(rec['position'], parts, orientation);     // find the zone the position belongs to
            // first occurrence for this zone
            if (!exists(rec['team_id'], ret[zone]['values'])) {
                ret[zone]['values'].push( {team: rec['team_id'], count: 1, perc: 0} );
            } else {
                ret[zone]['values'].forEach( val => {
                    if (val['team'] == rec['team_id']) {
                        val['count']++;
                    }
                });
            }
        });
    });

    // compute each percentage
    ret.forEach( zone => {
        zone['values'].forEach( team => {
            team['perc'] = getPercentage(team['count'], totalCount);
        });
    });

    return ret;
}


/**
 * 
 * @param {*} data 
 * @param {*} min 
 * @param {*} max 
 */
function getHPresence(data, min, max) {
    
    let interval = max - min;
    let parts = divideField(interval, min, max)
    let orientation = 'horizontal';
    let ret = createDataModel(orientation);
    let totalCount = 0;
    let ids = [];
    let tmpId;
    let zone;

    // cout occurences
    data.forEach(frame => {
        totalCount += frame['records'].length;
        frame['records'].forEach(rec => {
            // localise the zone which the position belongs to
            zone = locateZone(rec['position'], parts, orientation);
            tmpId = rec['team_id'];
            // get all team ids
            if (!ids.includes(tmpId)) 
                ids.push(tmpId);
            if (ret[zone].hasOwnProperty(tmpId)) {
                ret[zone][tmpId]['count'] ++;
            } else 
                ret[zone][tmpId] = {count: 1, perc: 0};
        });
    });

    // compute each percentage
    ret.forEach(zone => {
        
        for(let i = 0; i < ids.length; i++)
            zone[ids[i]]['perc'] = getPercentage(zone[ids[i]]['count'], totalCount);
    });

    return ret;
}


/**
 * 
 * @param {*} data 
 */
function getMaxPerSet(data) {

    let max = 0;
    data.forEach(zone => {
        for (const key in zone) {
            if (zone[key].constructor == Object && zone[key]['count'] > max) {  // check for each json object
                max = zone[key]['count'];
            }
        }
    });

    return max;
}