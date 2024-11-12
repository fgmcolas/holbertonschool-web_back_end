const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
	it('should return 6 for SUM of 1.4 and 4.5', () => {
		expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
	});
	it('should return -4 for SUBTRACT of 1.4 and 4.5', () => {
		expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
	});
	it('should return 0.2 for DIVIDE of 1.4 and 4.5', () => {
		expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
	});
	it('should return "Error" for DIVIDE by zero', () => {
		expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
	});
});
