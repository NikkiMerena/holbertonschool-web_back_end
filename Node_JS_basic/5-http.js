const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http
  .createServer((req, res) => {
    console.log(process.argv);
    switch (req.url) {
      case '/':
        res.end('Hello Holberton Scool!');
        break;
      case '/students':
        res.write('This is the list of our students\n');
        countStudents(process.argv[2])
          .then((data) => {
            const responseData = data.join('\n'); // Convert array to a single string
            res.end(responseData);
          })
          .catch((err) => res.end(err.message));
        break;
      default:
        break;
    }
  })
  .listen(1245);

module.exports = app;
