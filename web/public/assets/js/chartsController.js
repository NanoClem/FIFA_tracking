/**
 * 
 * @param {*} data 
 */
function updateCharts(data) {

    let colors = ['#e41a1c','#377eb8']

    // remove content of each chart
    d3.select("#vbarChartSVG").remove();
    d3.select("#hbarChartSVG").remove();
    d3.selectAll(".heatmap").remove();
    d3.select("#heatSlider").remove();

    // then update
    if (data.length > 0) {
        updateVpresence(780, 520, data, colors);
        updateHpresence(780, 520, data, colors);
        initHeatMaps(data);
    }
    
}


/**
 * 
 * @param {*} data 
 */
function upDateDashboard(data) {
    // console.log(data);
}


/**
 * 
 * @param {*} err 
 * @param {*} resData 
 */
function upDateAll(err, resData) {

    if (err) throw err;
    upDateDashboard(resData[1]);
    updateCharts(resData[0]);
}


/**
 * 
 * @param {*} element 
 */
function notifyChange(DOMelement) {

    var id = DOMelement.property("value");
    d3.queue()
        .defer(d3.json, "http://localhost:3000/api/frame/video/" + id)  // get all frame associated to this video
        .defer(d3.json, "http://localhost:3000/api/video/" + id)        // get data about the video
        .awaitAll(upDateAll)
}


/**
 * 
 * @param {*} url 
 */
function getAllVideos() {

    d3.json("http://localhost:3000/api/video", function (err, data) {
        if (err) throw err;

        // appending video as option to the selector
        var selector = d3.select("#vidList")
            // notify each change
            .on("change", function (d) { notifyChange(d3.select(this)); })
            // append all videos
            .selectAll(".myOptions")
            .data(data)
            .enter().append("option")
                .attr("value", function (d) { return d._id; })
                .text(function (d) { return d.title; });
    });
}

getAllVideos();