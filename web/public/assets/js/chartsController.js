/**
 * 
 * @param {*} data 
 */
function updateCharts(data, colors) {

    // remove content of each chart
    d3.select("#vbarChartSVG").remove();
    d3.select("#hbarChartSVG").remove();
    d3.selectAll(".heatmap").remove();
    d3.select("#heatSlider").remove();

    // then update
    if (data.constructor == Array && data.length > 0) {
        // find involved teams and filter duplicates
        updateVpresence(780, 520, data, colors);
        updateHpresence(780, 520, data, colors);
        initHeatMaps(data);
    }
}


/**
 * 
 * @param {*} data 
 */
function upDateTeamLabels(teamsData) {

    if (teamsData.constructor == Array && teamsData.length > 0) {
        // first team label
        d3.select("#lc1")
            .style("background-color", teamsData[0].jersey_color)
            .select(".teamLabel")
                .text(teamsData[0].name)
        // second team label
        d3.select("#lc2")
        .style("background-color", teamsData[1].jersey_color)
        .select(".teamLabel")
            .text(teamsData[1].name)
    }
}


/**
 * 
 * @param {*} err 
 * @param {*} resData 
 */
function upDateAll(err, resData) {

    if (err) throw err;

    // get involved teams data
    d3.json("http://localhost:3000/api/team/" + resData[1]['teams'][0] + "/" + resData[1]['teams'][1], function (err2, data) {
        if (err2) throw err2;

        let colors = data.map(function (d) { return d.jersey_color; });
        upDateTeamLabels(data);
        updateCharts(resData[0], colors);
    });
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
        .awaitAll(upDateAll);
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