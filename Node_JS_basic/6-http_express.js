const express = require('express');

// Create an Express application
const app = express();

// Define a route for the endpoint '/'
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start the HTTP server and listen on port 1245
const port = 1245;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Export the Express application
module.exports = app;
