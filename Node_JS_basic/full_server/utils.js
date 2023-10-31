const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n');
        const studentsByField = {};

        for (const line of lines) {
          const [firstname, , , field] = line.split(',');

          if (field && field.trim() !== '') {
            if (!studentsByField[field]) {
              studentsByField[field] = [];
            }
            studentsByField[field].push(firstname);
          }
        }

        resolve(studentsByField);
      }
    });
  });
}

module.exports = { readDatabase };
