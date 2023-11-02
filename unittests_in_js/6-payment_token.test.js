// async API testing
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('returns a resolved promise', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.eql({
          data: 'Successful response from the API',
        });
        done();
      })
      .catch((err) => {
        done(err);
      });
  });
});
