/**
 * Scale a number between a target range
 * @param {Number} n number to scale
 * @param {JSON} nRange range of the given number
 * @param {JSON} tRange targeted range
 * 
 * @returns an int between the targeted range
 */
function scaleInRange(n, nRange, tRange){

    let num = (n - nRange['min']) * (tRange['max'] - tRange['min']);
    let den = nRange['max'] - nRange['min'];

    return Math.floor(num/den + tRange['min']);
}


/**
 * Finds and returns both teams identifier in a records collection.
 * @param {Array} records
 */
function getTeams(records) {

    let ids = [],
        tmp = "";
    
    if (Array.isArray(records) && records.length > 0) {
        
        for (let i = 0; i < records.length; i++) {
            // both team are found
            if (ids.length == 2)
                return ids;
            // one or both team are missing
            tmp = records[i]['team_id']
            if (!ids.includes(tmp)) {
                ids.push(tmp);
            }
                
        }
    }
    
    return ids;
}


/**
 * Associate each positions to a team and find the maximum value for each axis
 * @param {*} data 
 */
function getPositionsPerTeam(data) {

    let p1 = [],                     // positions of team 1
        p2 = [],                     // positions of team 2
        xMax = 0,                    // maximum value for x pos
        yMax = 0,                    // maximum position for y pos
        rec = data[0]['records'],    // only need one records collection to find our team
        teams = getTeams(rec);       // get team ids
        

    if (Array.isArray(teams) && teams.length > 0) {
        data.forEach(frame => {
            frame['records'].forEach(rec => {
                // find maximum pos
                xMax = rec['position']['x'] > xMax ? rec['position']['x'] : xMax;
                yMax = rec['position']['y'] > yMax ? rec['position']['y'] : yMax;
                // associate positions to teams
                if (rec['team_id'] == teams[0])
                    p1.push(rec['position']);
                else
                    p2.push(rec['position']);
            });
        });
    }
    
    return { p1: p1, p2: p2, xMax: xMax, yMax: yMax};
}