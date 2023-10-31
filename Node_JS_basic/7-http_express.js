const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const databasePath = process.argv[2] || '';

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(databasePath)
    .then((data) => {
      const responseData = data.join('\n');
      res.end(responseData);
    })
    .catch((err) => res.end(err.message));
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
