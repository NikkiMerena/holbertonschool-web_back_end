// 2-read_file.js
// Using the database database.csv (provided in project description),
// create a function countStudents in the file 2-read_file.js

const fs = require('fs');

function countStudents(path) {
  try {
    // Read the contents of the database file synchronously.
    const data = fs.readFileSync(path, 'utf8');

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
  } catch (error) {
    // Handle errors, including the case when the database is not available.
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
