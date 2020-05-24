// DIMENSIONS
var margin = {top: 0, rigth: 30, bottom: 0, left: 40},
    width  = 1050 - margin.left - margin.rigth,
    height = 680 - margin.top - margin.bottom;

// color
var color = ['#e41a1c','#377eb8'];

// svg
var svg = d3.select("#hbarChart")
    .append("svg")
        .attr("width", width + margin.left + margin.rigth)
        .attr("height", height + margin.top + margin.bottom)
        .attr("id", "hbarChartSVG");

// plot
var plot = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


/*=======================================================================================
    ------------ GET DATA ------------ 
======================================================================================*/
d3.json("assets/datasets/chart_dataset.json", function(err, data) {
    if (err) throw err;

    // min
    var min = d3.min(data, function (records) {
        return d3.min(records.records, function (d) { return d.position.x });
    });

    // max
    var max = d3.max(data, function (records) {
        return d3.max(records.records, function (d) { return d.position.x });
    });

    // format dataset
    data = getHPresence(data, min, max);
    console.log(data);

    // seek maximum x scale value
    var xMax = getMaxPerSet(data);
    
    // all group names
    var groups = data.map(function (d) { return d.zone });
    
    // all subgroup names
    var subGroups = Object.keys(data[0]);
    subGroups = subGroups.filter(key => key !== "zone");    // remove "zone" key to keep only subgroups


    // SCALES AXIS
    // x scale
    var x = d3.scaleLinear()
        .range([0, width])
        .domain([-xMax, xMax]);
    // y scale
    var y = d3.scaleBand()
        .rangeRound([0, height])
        .domain(groups)
        .paddingInner(0.1)


    // DRAW CHART

    // left side
    plot.selectAll(".leftSide")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "leftSide")
            .attr("x", function (d) { return x(0) })
            .attr("y", function (d) { return y(d.zone) })
            .attr("width", function (d) { return width - x(0) })
            .attr("height", y.bandwidth())
            .style("fill", color[0]);

    // right side
    plot.selectAll(".rightSide")
        .data(data)
        .enter()
        .append("rect")
            .attr("class", "rightSide")
            .attr("x", function (d) { return x(0) })
            .attr("y", function (d) { return y(d.zone) })
            .attr("width", function (d) { return width + x(0) })
            .attr("height", y.bandwidth())
            .style("fill", color[1]);

    // ADD ANIMATION
    // left side
    plot.selectAll("rect.leftSide")
        .transition()
        .delay(function (d) { return Math.random()*500 })
        .duration(1000)
        .attr("x", function (d) { return x(Math.min(0, -d[subGroups[0]].count)) })
        .attr("width", function (d) { return Math.abs(x(-d[subGroups[0]].count) - x(0)) })
    // right side
    plot.selectAll("rect.rightSide")
        .transition()
        .delay(function (d) { return Math.random()*500 })
        .duration(1000)
        .attr("x", function (d) { return x(Math.min(0, d[subGroups[1]].count)) })
        .attr("width", function (d) { return Math.abs(x(d[subGroups[1]].count) - x(0)) })

    // ADD TEXT LABELS
    // left side
    plot.selectAll("leftSide.text")
        .data(data)
        .enter()
        .append("text")
            .text(function (d) { return formatAsInteger(d[subGroups[0]].perc) + "%" })
                .attr("x", function (d) { return x(-xMax/2) })
                .attr("y", function(d) {return y(d.zone) + y.bandwidth()/2})
                .attr("class", "Axis");
    // right side
    plot.selectAll("rightSide.text")
        .data(data)
        .enter()
        .append("text")
            .text(function (d) { return formatAsInteger(d[subGroups[1]].perc) + "%" })
                .attr("x", function (d) { return x(xMax/2) })
                .attr("y", function(d) {return y(d.zone) + y.bandwidth()/2})
                .attr("class", "Axis");
});