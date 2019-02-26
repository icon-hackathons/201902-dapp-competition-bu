express = require('express');
path = require('path');

var app = express();

app.use(express.static(path.join(__dirname, 'public')));

app.locals.pretty = true;

app.get('/', function(req, res) {
    res.render("index.html");
});

app.listen(3000, function() {
    console.log('Connected 3000 port!');
});