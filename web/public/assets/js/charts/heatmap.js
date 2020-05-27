/**
 * Create a heatmap based on the position of each player of a team
 * @param {*} config 
 * @param {*} positions 
 * @param {*} width 
 * @param {*} height 
 * @param {*} max 
 * @param {*} val 
 */
function createHeatmap(config, positions, width, height, max, val) {
  
  var heatmapInstance = h337.create(config);

  // now generate some random data
  var points = [];
  
  // heatmap ranges
  var heatWRange = { min: 0, max: width };
  var heatHRange = { min: 0, max: height };

  // set data range
  var dataWRange = { min: 0, max: positions['xMax'] };
  var dataHRange = { min: 0, max: positions['yMax']};

  positions['pos'].forEach(pos => {
    points.push({
      x : scaleInRange(pos['x'], dataWRange, heatWRange),
      y : scaleInRange(pos['y'], dataHRange, heatHRange),
      value : val
    });
  });

  var heatmapData = {
    max : max,
    data : points
  };
  
  heatmapInstance.setData(heatmapData);
  return heatmapInstance;
}


/* ==================================================
    ////////// OPERATIONS ON HEATMAPS //////////
===================================================*/
/**
 * Update each heat value in given heatmap data
 * @param {Array} data
 * @param {Number} new_value 
 */
function updateHeatValues(data) {

  let tmp = [];
  data.forEach(heatData => {
    tmp = heatData['data'];
    // set new heat value
    tmp['data'].forEach(point => {
      point['value'] = heatData['new_value'];
    });
    // update data and repaint the heatmap
    heatData['heatmap'].setData(tmp);
  });
}

/**
 * 
 */
function initHeatMaps() {
  // params
  var w = 525,
    h = 340,
    max = 100,
    val = 20,
    p = {};

  // configs
  var config1 = {
    container: document.getElementById('heatmap1')
  };
  var config2 = {
    container: document.getElementById('heatmap2')
  };

  // Import data
  d3.json("assets/datasets/chart_dataset.json", function(err, data) {
    if (err) throw err;

    // get every position by team
    p = getPositionsPerTeam(data);

    // heatmap instances
    let h1 = createHeatmap(config1, {pos: p['p1'], xMax: p['xMax'], yMax: p['yMax']}, w, h, max, val);
    let h2 = createHeatmap(config2, {pos: p['p2'], xMax: p['xMax'], yMax: p['yMax']}, w, h, max, val);


    // listening to heat slider change
    d3.select("#heatSlider").on("change", function (d) {

      // new slide value
      let newValue = this.value;

      // heatmap data
      let d1 = h1.getData();
      let d2 = h2.getData();

      let prepared = [
        {"heatmap": h1, "data": d1, "new_value": newValue},
        {"heatmap": h2, "data": d2, "new_value": newValue}
      ];
      
      // update heat values in each dataset
      updateHeatValues(prepared);
    })
    
  });
}

// 
initHeatMaps();
