/**
 * Format integer for printing
 */
var formatAsInteger = d3.format(",");


/**
 * Comoute the zones of the field
 * @param {Number} totalSize 
 * @param {Number} minSize 
 * @param {Number} maxSize 
 */
function divideField(totalSize, minSize, maxSize) {

    var div = totalSize/3;
    var first_tierce = div + minSize;
    var second_tierce = div * 2 + minSize;

    return [minSize, first_tierce, second_tierce, maxSize];
}


/**
 * Compute the zone of the field in which a postion is
 * @param {Object} position 
 * @param {Array} parts computed zones of the field
 * @param {String} orientation vertical or horizontal
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


/**
 * Tell if a team exists or not in a dataset (as an array)
 * @param {String} team 
 * @param {Array} array 
 * 
 * @returns true if exists, otherwise false
 */
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
 * Get the vertical presence ratio for each three zone of the field.
 * @param {JSON} data
 * @param {Number} min minimum y coord of the dataset
 * @param {Number} max maximum y coord of the dataset
 * 
 * @returns {JSON} new formatted dataset for vertical barchart visualization
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
 * Get the horizontal presence ratio for each three zone of the field.
 * @param {JSON} data
 * @param {Number} min minimum x coord of the dataset
 * @param {Number} max maximum x coord of the dataset
 * 
 * @returns {JSON} new formatted dataset for horizontal barchart visualization
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

    // count occurences
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
 * Get the maximum count value among all data sets
 * @param {JSON} data 
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