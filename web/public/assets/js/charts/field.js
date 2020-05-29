/**
 * Return all lines used to build the field.
 * This includes : goals, penalty boxes, six-yard boxes, outside borders, middle line
 * @param {*} plotWidth 
 * @param {*} plotHeight 
 */
function getPlotLines(plotWidth, plotHeight) {

    const lines = [];
    // left penalty box
    lines.push({x1: 0, x2: 16.5, y1: plotHeight/2 - 11 - 9.15, y2: plotHeight/2 - 11 - 9.15});
    lines.push({x1: 16.5, x2: 16.5, y1: 13.85, y2: plotHeight/2 + 11 + 9.15});
    lines.push({x1: 0, x2: 16.5, y1: plotHeight/2 + 11 + 9.15, y2: plotHeight/2 + 11 + 9.15});
    // left six-yard box
    lines.push({x1: 0, x2: 5.5, y1: plotHeight/2 - 9.15, y2: plotHeight/2 - 9.15});
    lines.push({x1: 5.5, x2: 5.5, y1: plotHeight/2 - 9.15, y2: plotHeight/2 + 9.15});
    lines.push({x1: 0, x2: 5.5, y1: plotHeight/2 + 9.15, y2: plotHeight/2 + 9.15});
    // right penalty box
    lines.push({x1: plotWidth - 16.5, x2: plotWidth, y1: plotHeight/2 - 11 - 9.15, y2: plotHeight/2 - 11 - 9.15});
    lines.push({x1: plotWidth - 16.5, x2: plotWidth - 16.5, y1: plotHeight/2 - 11 - 9.15, y2: plotHeight/2 + 11 + 9.15});
    lines.push({x1: plotWidth - 16.5, x2: plotWidth, y1: plotHeight/2 + 11 + 9.15, y2: plotHeight/2 + 11 + 9.15});
    // right six-yard box
    lines.push({x1: plotWidth - 5.5, x2: plotWidth, y1: plotHeight/2 - 9.15, y2: plotHeight/2 - 9.15});
    lines.push({x1: plotWidth - 5.5, x2: plotWidth - 5.5, y1: plotHeight/2 - 9.15, y2: plotHeight/2 + 9.15});
    lines.push({x1: plotWidth - 5.5, x2: plotWidth, y1: plotHeight/2 + 9.15, y2: plotHeight/2 + 9.15});
    // outside borders
    lines.push({x1: 0, x2: plotWidth, y1: 0, y2: 0});
    lines.push({x1: 0, x2: plotWidth, y1: plotHeight, y2: plotHeight});
    lines.push({x1: 0, x2: 0, y1: 0, y2: plotHeight});
    lines.push({x1: plotWidth, x2: plotWidth, y1: 0, y2: plotHeight});
    // middle line
    lines.push({x1: plotWidth/2, x2: plotWidth/2, y1: 0, y2: plotHeight});
    // left goal
    lines.push({x1: -1.5, x2: -1.5, y1: plotHeight/2 - 7.32/2, y2: plotHeight/2 + 7.32/2});
    lines.push({x1: -1.5, x2: 0, y1: plotHeight/2 - 7.32/2, y2: plotHeight/2 - 7.32/2});
    lines.push({x1: -1.5, x2: 0, y1: plotHeight/2 + 7.32/2, y2: plotHeight/2 + 7.32/2});
    // right goal
    lines.push({x1: plotWidth + 1.5, x2: plotWidth + 1.5, y1: plotHeight/2 - 7.32/2, y2: plotHeight/2 + 7.32/2});
    lines.push({x1: plotWidth, x2: plotWidth + 1.5, y1: plotHeight/2 - 7.32/2, y2: plotHeight/2 - 7.32/2});
    lines.push({x1: plotWidth, x2: plotWidth + 1.5, y1: plotHeight/2 + 7.32/2, y2: plotHeight/2 + 7.32/2});

    return lines;
}


/**
 * Return all circles used to build the field.
 * This includes : center circle, penalty spots, kick-off circle
 * @param {*} plotWidth 
 * @param {*} plotHeight 
 * @param {*} lineColor 
 */
function getPlotCircles(plotWidth, plotHeight, lineColor) {

    const circles = [];
    circles.push({cx: plotWidth/2, cy: plotHeight/2, r: 9.15, color: 'none'});          // center circle
    circles.push({cx: 11, cy: plotHeight/2, r: 0.3, color: lineColor});                 // left penalty spot
    circles.push({cx: plotWidth - 11, cy: plotHeight/2, r: 0.3, color: lineColor});     // right penalty spot
    circles.push({cx: plotWidth/2, cy: plotHeight/2, r: 0.3, color: lineColor});        // kick-off circle
    
    return circles;
};


/**
 * Returns all arcs used to build the field.
 * This includes : penalty arcs, corners
 * @param {*} plotWidth 
 * @param {*} plotHeight 
 * @param {*} scaling 
 * @param {Number} lineThick
 */
function getArcs(plotWidth, plotHeight, scaling, lineThick) {

    const arcs = [];
    const cornerRadius = 1 * scaling;
    const penaltyRadius = 9.15 * scaling;

    // left top corner
    arcs.push({arc: {innerRadius: cornerRadius, outerRadius: cornerRadius + lineThick, startAngle: 1/2 * Math.PI, endAngle: Math.PI}, 'x': 0, 'y': 0});
    // left bottom corner
    arcs.push({arc: {innerRadius: cornerRadius, outerRadius: cornerRadius + lineThick, startAngle: 1/2 * Math.PI, endAngle: 0}, 'x': 0, 'y': plotHeight});
    // right top corner
    arcs.push({arc: {innerRadius: cornerRadius, outerRadius: cornerRadius + lineThick, startAngle: 3/2 * Math.PI, endAngle: Math.PI}, 'x': plotWidth, 'y': 0});
    // right bottom corner
    arcs.push({arc: {innerRadius: cornerRadius, outerRadius: cornerRadius + lineThick, startAngle: 2 * Math.PI, endAngle: 3/2 * Math.PI}, 'x': plotWidth, 'y': plotHeight});
    // left penalty arc
    arcs.push({arc: {innerRadius: penaltyRadius, outerRadius: penaltyRadius + lineThick, startAngle: Math.sin(6.5/9.15), endAngle: Math.PI - Math.sin(6.5/9.15)}, 'x': 11, 'y': plotHeight/2});
    // right penalty arc
    arcs.push({arc: {innerRadius: penaltyRadius, outerRadius: penaltyRadius + lineThick, startAngle: -Math.sin(6.5/9.15), endAngle: -(Math.PI - Math.sin(6.5/9.15))}, 'x': plotWidth - 11, 'y': plotHeight/2});
    
    return arcs;
}

/**
 * 
 * @param {*} divID 
 * @param {*} margin 
 * @param {*} width 
 * @param {*} height 
 * @param {*} lineColor 
 * @param {*} fillColor 
 * @param {*} lineThick 
 */
function createField(divID, margin, width, height, scaling, lineColor, fillColor, lineThick) {

    // plot dims
    var plotW = 105,
        plotH = 68;
        plotScale = scaling;

    // create svg
    var svg = d3.select(divID)
        .append("svg")
        .attr("width", width + margin.left + margin.rigth)
        .attr("height", height + margin.top + margin.bottom)

    // field plot
    var plot = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // main rect field
    plot.append("rect")
        .attr("x", -margin.left)
        .attr("y", -margin.top)
        .attr("width", width + margin.left + margin.rigth)
        .attr("height", height + margin.top + margin.bottom)
        .attr("fill", fillColor);

    // all plot lines data
    var plotLines = getPlotLines(plotW, plotH);
    plot.selectAll(".plotLines")
        .data(plotLines)
        .enter().append("line")
            .attr('x1', d => d['x1'] * plotScale)
            .attr('x2', d => d['x2'] * plotScale)
            .attr('y1', d => d['y1'] * plotScale)
            .attr('y2', d => d['y2'] * plotScale)
            .style('stroke-width', lineThick)
            .style('stroke', lineColor);

    // all plot circles data
    var plotCircles = getPlotCircles(plotW, plotH, lineColor);
    plot.selectAll(".plotCircles")
        .data(plotCircles)
        .enter().append("circle")
            .attr('cx', d => d['cx'] * plotScale)
            .attr('cy', d => d['cy'] * plotScale)
            .attr('r', d => d['r'] * plotScale)
            .style('stroke-width', lineThick)
            .style('stroke', lineColor)
            .style('fill', d => d['color']);

    // all plot arcs data
    var plotArcs = getArcs(plotW, plotH, plotScale, lineThick);
    var arc = d3.arc();
    plot.selectAll(".plotArcs")
        .data(plotArcs)
        .enter().append("path")
            .attr('d', d => arc(d['arc']))
            .attr('transform', d => "translate(" + plotScale * d.x + "," + plotScale * d.y + ")")
            .style('fill', lineColor);
}


/* ==================================================
    ////////// INIT FIELDS //////////
===================================================*/

/**
 * Init all field charts
 */
function initFields() {

    // params
    var lineColor = "#ffffff";   
    var fillColor = "#5aac44";
    var lineThick = 2;

    // dimensions
    var margin = {top: 20, rigth: 20, bottom: 20, left: 20},
        w = 525,
        h = 340,
        scale = 5;

    // fields
    createField("#f1", margin, w, h, scale,lineColor, fillColor, lineThick);
    createField("#f2", margin, w, h, scale,lineColor, fillColor, lineThick);
    createField("#f3", margin, 740, 480, 7, lineColor, fillColor, lineThick);
    createField("#f4", margin, 740, 480, 7, lineColor, fillColor, lineThick);
}

initFields();
