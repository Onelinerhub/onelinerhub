# How do I use PHP Omnipay with Node.js?
// plain

Using PHP Omnipay with Node.js is possible, though there are some additional steps to take.

1. Install the Omnipay library for Node.js. This can be done with the command `npm install omnipay`.
2. Create a file to store your payment gateway credentials (e.g., `credentials.js`).

```javascript
module.exports = {
  gateway: {
    username: 'yourUsername',
    password: 'yourPassword'
  }
};
```

3. Import the credentials into your Node.js script.

```javascript
const credentials = require('./credentials');
```

4. Create an Omnipay gateway object.

```javascript
const gateway = require('omnipay').gateway('YourGatewayName', {
  username: credentials.gateway.username,
  password: credentials.gateway.password
});
```

5. Set the parameters for the payment request.

```javascript
const paymentData = {
  amount: '10.00',
  currency: 'USD',
  card: {
    number: '4111111111111111',
    expiryMonth: '10',
    expiryYear: '2022',
    cvv: '123'
  }
};
```

6. Send the payment request.

```javascript
gateway.purchase(paymentData).then(function (response) {
  console.log('Payment successful!');
});
```

7. Handle the response.

```javascript
gateway.on('complete', function (data) {
  if (data.success) {
    console.log('Payment was successful');
  } else {
    console.log('Payment failed');
  }
});
```

## Helpful links

- [Omnipay documentation](https://omnipay.thephpleague.com/getting-started/)
- [Node.js documentation](https://nodejs.org/en/docs/)

onelinerhub: [How do I use PHP Omnipay with Node.js?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-with-node-js)