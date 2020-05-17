const express = require('express');
const http = require('http');
const reload = require('reload');
const app = express();

const PORT = 5000;


// PARSER FOR JSON DATA
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded ( {
	extended : true
}));
app.use(bodyParser.json());


// CONFIGURE SERVER
app.set('view engine', 'ejs');
app.set('views', './public/views');
app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => res.render('index'));

// START SERVER
const server = http.createServer(app);
server.listen(PORT, () => console.log("waiting on http://localhost:" + PORT));
reload(app);



