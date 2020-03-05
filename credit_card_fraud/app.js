var express = require('express');
var bodyParser = require('body-parser');
var cors = require('cors');
var app = express();

app.use(bodyParser.json());
app.options('*', cors());
app.use(cors());

app.get('/api/date', function (req, res, next) {

  var g = req.query;
  var asJSON = JSON.stringify(g);

  const { spawn } = require('child_process');
  const pyProg = spawn('python', ['./model.py', asJSON]);
  
  pyProg.stdout.on('data', function (data) {
    console.log("class value :", data.toString())
    return res.send(data);

  })
});
app.listen(3000)

