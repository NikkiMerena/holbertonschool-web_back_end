// full_server/server.js

const express = require('express');
const path = require('path');
const routes = require('./routes');

const app = express();

// Define the database file path
app.use((req, res, next) => {
  req.dbFilePath = path.join(__dirname, 'database.csv');
  next();
});

// Use the routes
app.use('/', routes);

// Start the server
const port = 1245;
app.listen(port, () => {
console.log(`Server is running on port ${port}`);
});

module.exports = app;
