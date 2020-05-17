var heatmapContainer = document.getElementById('heatmap');

// create instance
var heatmapInstance = h337.create({
    container: heatmapContainer,
    radius: 90
  });

heatmapContainer.onmousemove = function(ev) {
    heatmapInstance.addData({
        x: ev.layerX,
        y: ev.layerY,
        value: 1
    });
};