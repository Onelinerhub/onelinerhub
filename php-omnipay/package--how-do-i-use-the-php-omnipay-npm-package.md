# package

How do I use the PHP Omnipay NPM package?
// plain

The PHP Omnipay NPM package is a package for processing payments using the Omnipay library. It is a wrapper around the Omnipay library, allowing developers to easily integrate payment processing into their applications.

To use the package, first install it using the NPM command:
```
npm install omnipay
```

Then, you can require the package in your application and begin using it:
```
const Omnipay = require('omnipay');

let gateway = Omnipay.create('PayPal_Express');
```

The gateway object can then be used to process payments. For example, to process a payment with the PayPal Express gateway, you can do the following:

```
gateway.purchase({
  amount: '10.00',
  currency: 'USD',
  returnUrl: 'http://www.example.com/return',
  cancelUrl: 'http://www.example.com/cancel'
}).then(function (response) {
  // Process the response
});
```

The response will contain the payment details, such as the transaction ID, payment status, and other information.

For more information about using the package, please refer to the [Omnipay NPM package documentation](https://www.npmjs.com/package/omnipay).

onelinerhub: [package

How do I use the PHP Omnipay NPM package?](https://onelinerhub.com/php-omnipay/package--how-do-i-use-the-php-omnipay-npm-package)