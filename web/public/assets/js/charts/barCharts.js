// Getting our dataset
d3.json("http://localhost:3000/api/frame?video_id=5ecdcc69521f95f867ba1eaa", function(err, data) {
    if (err) throw err;

    let colors = ['#e41a1c','#377eb8']
    plotVpresence(780, 520, data, colors);
    plotHpresence(780, 520, data, colors);
});