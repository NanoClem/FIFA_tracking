// var heatmapContainer = document.getElementById('heatmap');

// // create instance
// var heatmapInstance = h337.create({
//     container: heatmapContainer,
//     radius: 90
//   });

// document.getElementById('field').onmousemove = function(ev) {
//     heatmapInstance.addData({
//         x: ev.layerX,
//         y: ev.layerY,
//         value: 1
//     });
// };

// minimal heatmap instance configuration
var heatmapInstance = h337.create({
    // only container is required, the rest will be defaults
    container: document.getElementById('heatmap')
  });
  
  // now generate some random data
  var points = [];
  var max = 0;
  var width = 1050;
  var height = 680;
  var len = 200;
  
  while (len--) {
    var val = Math.floor(Math.random()*100);
    max = Math.max(max, val);
    var point = {
      x: Math.floor(Math.random()*width),
      y: Math.floor(Math.random()*height),
      value: val
    };
    points.push(point);
  }
  // heatmap data format
  var data = {
    max: max,
    data: points
  };
  // if you have a set of datapoints always use setData instead of addData
  // for data initialization
  heatmapInstance.setData(data);