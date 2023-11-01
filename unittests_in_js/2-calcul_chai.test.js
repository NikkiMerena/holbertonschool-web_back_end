const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  it('should add two numbers when type is SUM', () => {
    const result = calculateNumber('SUM', 1.4, 4.5);
    expect(result).to.equal(6);
  });

  it('should subtract two numbers when type is SUBTRACT', () => {
    const result = calculateNumber('SUBTRACT', 1.4, 4.5);
    expect(result).to.equal(-4);
  });

  it('should divide two numbers when type is DIVIDE', () => {
    const result = calculateNumber('DIVIDE', 1.4, 4.5);
    expect(result).to.equal(0.2);
  });

  it('should return "Error" when dividing by 0', () => {
    const result = calculateNumber('DIVIDE', 1.4, 0);
    expect(result).to.equal('Error');
  });

  it('should throw an error for an invalid type', () => {
    expect(() => calculateNumber('INVALID', 1.4, 4.5)).to.throw(/Invalid type/);
  });
});
