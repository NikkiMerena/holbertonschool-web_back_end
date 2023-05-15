export default function divideFunction(numerator, denominator) {
  // Function to divide two numbers

  if (denominator === 0) {
    // Check if the denominator is equal to 0
    // If it is, throw an Error with the message 'cannot divide by 0'
    throw new Error('cannot divide by 0');
  }

  return (numerator / denominator);
  // Return the result of dividing the numerator by the denominator
}
