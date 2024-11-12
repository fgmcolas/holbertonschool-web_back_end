const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
	let consoleSpy;

	beforeEach(() => {
		consoleSpy = sinon.spy(console, 'log');
	});

	afterEach(() => {
		consoleSpy.restore();
	});

	it('logs correct message for 100 and 20', () => {
		sendPaymentRequestToApi(100, 20);
		sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 120');
	});

	it('logs correct message for 10 and 10', () => {
		sendPaymentRequestToApi(10, 10);
		sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 20');
	});
});
