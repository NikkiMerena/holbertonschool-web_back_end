// 3-payment.test.js

const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const { Utils } = require('./utils');

describe('sendPaymentRequestToApi', () => {

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

  it('should call Utils.calculateNumber with correct arguments', () => {
    // Create a spy on Utils.calculateNumber
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    // Call sendPaymentRequestToApi
    sendPaymentRequestToApi(100, 20);

    // Expect the spy to have been called with the correct arguments
    sinon.assert.calledWith(calculateNumberSpy, 'SUM', 100, 20);

    // Restore the spy to its original state
    calculateNumberSpy.restore();
  });
});
