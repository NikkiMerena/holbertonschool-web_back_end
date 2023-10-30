const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Attempt to read the database file asynchronously.
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        // If there's an error reading the file, reject the Promise.
        reject(new Error('Cannot load the database'));
      } else {
        // Split the data into lines.
        const lines = data.split('\n');

        // Initialize variables to count students in each field.
        let totalStudents = 0;
        let csStudents = 0;
        let sweStudents = 0;
        const csList = [];
        const sweList = [];

        // Loop through each line and process student data.
        for (const line of lines) {
          const [firstname, lastname, age, field] = line.split(',');

          // Check if the line contains valid student data.
          if (firstname && lastname && age && field) {
            totalStudents += 1;

            if (field === 'CS') {
              csStudents += 1;
              csList.push(firstname);
            } else if (field === 'SWE') {
              sweStudents += 1;
              sweList.push(firstname);
            }
          }
        }

        // Log the results.
        console.log(`Number of students: ${totalStudents}`);
        console.log(`Number of students in CS: ${csStudents}. List: ${csList.join(', ')}`);
        console.log(`Number of students in SWE: ${sweStudents}. List: ${sweList.join(', ')}`);

        // Resolve the Promise.
        resolve();
      }
    });
  });
}

module.exports = countStudents;
