/**
 * Create a new football field
 * @param {String} divID id of the div where the chart should be drawn
 */
function createField(divID, width, height, lineColor, fillColor, thickness) {

    var svg = d3.select(divID) 
    .append("svg")    
    .attr("width", width)      
    .attr("height", height);
            
    // Total Grass    
    svg.append("rect")        // attach a rectangle
    .attr("x", 0)         // position the left of the rectangle
    .attr("y", 0)          // position the top of the rectangle
    .attr("height", height)    // set the height
    .attr("width", width)    // set the width
    .style("fill", fillColor);   // set the fill colour    

    // draw a rectangle pitch outline    
    svg.append("rect")        // attach a rectangle
    .attr('class', 'half-field')
    .attr("x", 50)         // position the left of the rectangle
    .attr("y", 50)          // position the top of the rectangle
    .attr("height", 680)    // set the height
    .attr("width", 1050)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)   // set the line colour
    .style("fill", fillColor);    // set the fill colour     

    // draw a rectangle - half 1
    svg.append("rect")        // attach a rectangle
    .attr("x", 50)         // position the left of the rectangle
    .attr("y", 50)          // position the top of the rectangle
    .attr("height", 680)    // set the height
    .attr("width", 525)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)   // set the line colour
    .style("fill", "none");    // set the fill colour


    // draw a rectangle - half 2
    svg.append("rect")        // attach a rectangle
    .attr("x", 575)         // position the left of the rectangle
    .attr("y", 50)          // position the top of the rectangle
    .attr("height", 680)    // set the height
    .attr("width", 525)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour 


    // draw a circle - center circle
    svg.append("circle")          // attach a circle
    .attr("cx", 575)             // position the x-centre
    .attr("cy", 390)             // position the y-centre
    .attr("r", 91.5)               // set the radius
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)      // set the line colour
    .style("fill", "none");     // set the fill colour


    // draw a rectangle - penalty area 1
    svg.append("rect")        // attach a rectangle
    .attr("x", 50)         // position the left of the rectangle
    .attr("y", 188.5)          // position the top of the rectangle
    .attr("height", 403)    // set the height
    .attr("width", 165)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour 


    // draw a rectangle - penalty area 2
    svg.append("rect")        // attach a rectangle
    .attr("x", 935)         // position the left of the rectangle
    .attr("y", 188.5)          // position the top of the rectangle
    .attr("height", 403)    // set the height
    .attr("width", 165)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour 

    // draw a rectangle - six yard box 1
    svg.append("rect")        // attach a rectangle
    .attr("x", 50)         // position the left of the rectangle
    .attr("y", 298.5)          // position the top of the rectangle
    .attr("height", 183)    // set the height
    .attr("width", 55)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour 

    // draw a rectangle - six yard box 2
    svg.append("rect")        // attach a rectangle
    .attr("x", 1045)         // position the left of the rectangle
    .attr("y", 298.5)          // position the top of the rectangle
    .attr("height", 183)    // set the height
    .attr("width", 55)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour 

    // draw a rectangle - goalmouth 1
    svg.append("rect")        // attach a rectangle
    .attr("x", 25)         // position the left of the rectangle
    .attr("y", 353.4)          // position the top of the rectangle
    .attr("height", 73.2)    // set the height
    .attr("width", 25)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour
    
    // draw a rectangle - goalmouth 2
    svg.append("rect")        // attach a rectangle
    .attr("x", 1100)         // position the left of the rectangle
    .attr("y", 353.4)          // position the top of the rectangle
    .attr("height", 73.2)    // set the height
    .attr("width", 25)    // set the width
    .style("stroke-width", thickness)    // set the stroke width
    .style("stroke", lineColor)    // set the line colour
    .style("fill", "none");    // set the fill colour


    // draw a circle - penalty spot 1
    svg.append("circle")        // attach a circle
    .attr("cx", 160)           // position the x-centre
    .attr("cy", 390)           // position the y-centre
    .attr("r", 5)             // set the radius
    .style("fill", lineColor);     // set the fill colour

    // draw a circle - penalty spot 2
    svg.append("circle")        // attach a circle
    .attr("cx", 990)           // position the x-centre
    .attr("cy", 390)           // position the y-centre
    .attr("r", 5)             // set the radius
    .style("fill", lineColor);     // set the fill colour

    // draw a circle - center spot
    svg.append("circle")        // attach a circle
    .attr("cx", 575)           // position the x-centre
    .attr("cy", 390)           // position the y-centre
    .attr("r", 5)             // set the radius
    .style("fill", lineColor);     // set the fill colour
    
    var arc = d3.arc()
    .innerRadius(89)
    .outerRadius(94)
    .startAngle(0.64) //radians
    .endAngle(2.5) //just radians
    
    var arc2 = d3.arc()
    .innerRadius(89)
    .outerRadius(94)
    .startAngle(-0.64) //radians
    .endAngle(-2.5) //just radians

    svg.append("path")
    .attr("d", arc)
    .attr("fill", lineColor)
    .attr("transform", "translate(160,390)")
    .attr("stroke-width", thickness)    // set the stroke width
    
    svg.append("path")
    .attr("d", arc2)
    .attr("fill", lineColor)
    .attr("transform", "translate(990,390)")
    .attr("stroke-width", thickness)    // set the stroke width
}


/* ==================================================
    ////////// CREATE FIELDS //////////
===================================================*/
// params
var lineColor = "#ffffff";   
var fillColor = "#5aac44";
var lineThick = 2;

// dimensions
var w = 1150;
var h = 780;

// fields
createField("#f1", w, h, lineColor, fillColor, lineThick);
createField("#f2", w, h, lineColor, fillColor, lineThick);
createField("#f3", w, h, lineColor, fillColor, lineThick);
createField("#f4", w, h, lineColor, fillColor, lineThick);