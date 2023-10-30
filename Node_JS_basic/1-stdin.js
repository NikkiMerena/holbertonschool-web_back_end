// 1-stdin.js

// Display a message to the user.
console.log('Welcome to Holberton School, what is your name?');

// Set up an event listener for when data is readable on the standard input (keyboard input).
process.stdin.on('data', (data) => {
  // Remove any trailing newline characters and store the input in a variable.
  const name = data.toString().trim();

  // Check if the input is not empty.
  if (name !== '') {
    // Display the user's name.
    console.log(`Your name is: ${name}`);
  }
});

// Set up an event listener for when the standard input ends.
process.stdin.on('end', () => {
  // Display a closing message when the input ends.
  console.log('This important software is now closing');
});

// Listen for input from the command line.
process.stdin.resume();
