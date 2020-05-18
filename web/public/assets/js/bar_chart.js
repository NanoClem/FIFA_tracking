var formatAsInteger = d3.format(",");
var colors = ["#ffffd9", "#edf8b1", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#253494", "#081d58"];


/**
 * Create bar chart dimensions
 */
function createDims() {

    var margin = {top: 30, rigth: 0, bottom: 20, left: 0},
        width  = 1050 - margin.left - margin.rigth,
        height = 400 - margin.top - margin.bottom,
        colorBar = d3.scale.category20(),
        barPadding = 0;

    return {
        margin: margin,
        width: width,
        height: height,
        colorBar: colorBar,
        barPadding: barPadding
    };
}

/**
 * Create bar chart
 */
function barChart() {

    // dimensions
    var dims = createDims();
    var margin = dims.margin,
        width  = dims.width,
        height = dims.height,
        colorBar = dims.colorBar,
        barPadding = dims.barPadding

    // scaling
    var xScale = d3.scale.linear().range([0, width]);
    var yScale = d3.scale.linear().range([height, 0]);

    // svg
    var svg = d3.select("#barChart")
        .append("svg")
            .attr("width", width + margin.left + margin.rigth)
            .attr("height", height + margin.top + margin.bottom)
            .attr("id", "barChartSVG");

    var plot = svg
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // get data
    d3.json("assets/datasets/data_bar.json", function(err, data) {
        if (err) throw err;

        // colors
        var colorScale = d3.scale.quantile()
            .domain([0, colors.length-1, d3.max(data, function(d) {
                return d.count;
            })])
            .range(colors);

        // axis domains
        xScale.domain([0, data.length]);
        yScale.domain([0, d3.max(data, function (d) { return d.count; })]);

        // add rect
        plot.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
                .attr("x", function (d, i) { return xScale(i) })
                .attr("width", width / data.length - barPadding)
                .attr("y", function (d) { return yScale(d.count); })
                .attr("height", function (d) { return height-yScale(d.count); })
                .attr("fill", function (d) {
                    return colorScale(d.count);
                });

        // add y labels to plot
        plot.selectAll("text")
        .data(data)
        .enter()
        .append("text")
            .text(function (d) { return formatAsInteger(d3.round(d.perc)) + "%";} )
            .attr("text-anchor", "middle")
            // Set x position to the left edge of each bar plus half the bar width
            .attr("x", function (d, i) {
                return (i * (width / data.length)) + ((width / data.length - barPadding) / 2);
            })
            .attr("y", function (d) { return yScale(d.count) + 30;} )
            .attr("class", "yAxis");

        // add x label to chart
        var xLabels = svg
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + (margin.top + height)  + ")");

        xLabels.selectAll("text.xAxis")
            .data(data)
            .enter()
            .append("text")
            .text(function (d) { return d.zone;})
            // Set x position to the left edge of each bar plus half the bar width
            .attr("x", function (d, i) {
                return (i * (width / data.length)) + ((width / data.length - barPadding) / 2);  
            })
            .attr("y", 15)
            .attr("class", "xAxis")
    });
}


// Plot chart
barChart();