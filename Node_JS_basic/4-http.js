const http = require('http');

// Create an HTTP server.
const app = http.createServer((req, res) => {
  // Set the response status and headers.
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send the response body.
  res.end('Hello Holberton School!\n');
});

// Listen on port 1245.
const port = 1245;
app.listen(port);

// Export the app variable.
module.exports = app;
