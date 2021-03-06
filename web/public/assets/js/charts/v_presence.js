/**
 * Plot the bar chart which represents the vertical presence
 * @param {*} w 
 * @param {*} h 
 * @param {*} data 
 */
function updateVpresence(w, h, data, colors) {

    // dimensions
    var margin = {top: 380, rigth: 25, bottom: 60, left: 20},
        width  = w - margin.left - margin.rigth,
        height = h - margin.top - margin.bottom,
        barPadding = 0.05;
        groupedBarPadding = 0;

    // color
    var color = d3.scaleOrdinal()
        .range(colors);

    // svg
    d3.select("#vbarChartSVG").remove();
    var svg = d3.select("#vbarChart")
        .append("svg")
            .attr("width", width + margin.left + margin.rigth)
            .attr("height", height + margin.top + margin.bottom)
            .attr("id", "vbarChartSVG");

    var plot = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        
    /*=======================================================================================
     * ------------ PLOT CHART ------------ 
     =======================================================================================*/

    // min
    var min = d3.min(data, function (records) {
        return d3.min(records.records, function (d) { return d.position.y });
    });

    // max
    var max = d3.max(data, function (records) {
        return d3.max(records.records, function (d) { return d.position.y });
    });

    
    // format dataset
    data = getVPresence(data, min, max);
    
    var groups = data.map(function (d) { return d.zone });
    var subGroups = data[0].values.map(function (d) { return d.team; });

    // maximum y scale value
    var yMax = d3.max(data, function (zones) {
        return d3.max(zones.values, function (d) { return d.count; });
    });

    var x0 = d3.scaleBand()
        .rangeRound([0, width])
        .domain(groups)
        .paddingInner(barPadding);

    var x1 = d3.scaleBand()
        .domain(subGroups)
        .rangeRound([0, x0.bandwidth()])
        .paddingInner(groupedBarPadding);

    var y = d3.scaleLinear()
        .range([height, 0])
        .domain([0, yMax]);

    var slice = plot.selectAll(".slice")
        .data(data)
        .enter()
        .append("g")
            .attr("transform", function(d) { return "translate(" + x0(d.zone) + ",0)"; });

    slice.selectAll("rect")
        .data(function (d) { return d.values; })
        .enter()
        .append("rect")
            .attr("x", function (d) { return x1(d.team); })
            .attr("y", function (d) { return y(0); })
            .attr("width", x1.bandwidth())
            .attr("height", function (d) { return height - y(0); })
            .style("fill", function(d) { return color(d.team); });

    // ADD ANIMATION
    slice.selectAll("rect")
        .transition()
        .delay(function (d) {return Math.random()*500;})
        .duration(1000)
        .attr("y", function(d) { return y(d.count); })
        .attr("height", function(d) { return height - y(d.count); });

    
    //add y labels to plot
    slice.selectAll("text")
    .data(function (d) { return d.values; })
    .enter()
    .append("text")
        .text(function (d) { return formatAsInteger(d.perc) + "%";} )
            .attr("x", function (d) {return x1(d.team) + x1.bandwidth()/2;})
            .attr("y", function (d) { return y(0) + 25 } )
            .attr("class", "Axis");

    plot.exit().remove();
}