const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
	it('uses stub for Utils.calculateNumber', () => {
		const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
		const consoleSpy = sinon.spy(console, 'log');

		sendPaymentRequestToApi(100, 20);

		sinon.assert.calledWithExactly(stub, 'SUM', 100, 20);
		sinon.assert.calledWithExactly(consoleSpy, 'The total is: 10');

		stub.restore();
		consoleSpy.restore();
	});
});
