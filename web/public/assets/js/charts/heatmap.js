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
 * @param {*} heatmaps 
 */
function listenHeatChange(heatmaps) {

  let newValue = document.getElementById("heatSlider").value;
  let preparedData = [];
  let tmpData = [];

  heatmaps.forEach(h => {
    tmpData = h.getData();
    preparedData.push( {"heatmap": h, "data": tmpData, "new_value": newValue} );
  });

  updateHeatValues(preparedData);
}

/**
 * 
 */
function initHeatMaps(data) {

  // params
  var w = 525,
    h = 340,
    max = 100,
    val = 20,
    p = {};

  // create divs to contain each heatmaps
  // first div
  d3.select("#hc1")
    .append("div")
      .attr("id", "heatmap1")
      .attr("class", "heatmap")
  // second div
  d3.select("#hc2")
    .append("div")
      .attr("id", "heatmap2")
      .attr("class", "heatmap")

  // configs
  var config1 = {
    container: document.getElementById('heatmap1')
  };
  var config2 = {
    container: document.getElementById('heatmap2')
  };

  // get every position by team
  p = getPositionsPerTeam(data);

  // heatmap instances
  let h1 = createHeatmap(config1, {pos: p['p1'], xMax: p['xMax'], yMax: p['yMax']}, w, h, max, val);
  let h2 = createHeatmap(config2, {pos: p['p2'], xMax: p['xMax'], yMax: p['yMax']}, w, h, max, val);

  // creating heat slider
  d3.select("#heatSlider").remove();
  d3.select("#heatUpdater")
    .append("input")
      .attr("type", "range")
      .attr("name", "heatSlider")
      .attr("min", 0)
      .attr("max", max)
      .attr("step", "1")
      .attr("value", val)
      .attr("id", "heatSlider")
      .on("input", function (d) {
        listenHeatChange([h1, h2]);
      });
}