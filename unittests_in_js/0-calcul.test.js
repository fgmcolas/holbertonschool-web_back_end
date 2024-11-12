const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
	it('should return 4 when inputs are (1, 3)', () => {
		assert.strictEqual(calculateNumber(1, 3), 4);
	});

	it('should return 5 when inputs are (1, 3.7)', () => {
		assert.strictEqual(calculateNumber(1, 3.7), 5);
	});

	it('should return 5 when inputs are (1.2, 3.7)', () => {
		assert.strictEqual(calculateNumber(1.2, 3.7), 5);
	});

	it('should return 6 when inputs are (1.5, 3.7)', () => {
		assert.strictEqual(calculateNumber(1.5, 3.7), 6);
	});

	it('should handle negative numbers correctly', () => {
		assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
	});

	it('should round up and down properly', () => {
		assert.strictEqual(calculateNumber(1.4, 4.5), 6);
	});

	it('should handle zero inputs correctly', () => {
		assert.strictEqual(calculateNumber(0, 0), 0);
	});
});
