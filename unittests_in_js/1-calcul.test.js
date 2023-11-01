// Set of unit tests for the calculateNumber function

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should add two numbers when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6); // Adds two numbers
  });

  it('should subtract two numbers when type is SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4); // Subtracts two numbers
  });

  it('should divide two numbers when type is DIVIDE', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2); // Divides two numbers
  });

  it('should return "Error" when dividing by 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error'); // Handles divison by 0
  });

  it('should throw an error for an invalid type', () => {
    assert.throws(() => calculateNumber('INVALID', 1.4, 4.5), /Invalid type/); // Throws error for invalid type
  });
});
