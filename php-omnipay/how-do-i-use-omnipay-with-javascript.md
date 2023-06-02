# How do I use Omnipay with JavaScript?
// plain

Omnipay is a payment processing library for PHP that can be used to integrate payment gateways into an application. It can also be used with JavaScript to process payments on the client side.

To use Omnipay with JavaScript, you need to include the Omnipay library in your HTML page and create an instance of the Omnipay gateway you want to use.

```html
<script src="https://example.com/omnipay.js"></script>
<script>
  var gateway = Omnipay.create('PayPal_Express');
</script>
```

You can then use the gateway instance to set up the payment details and initiate the payment.

```javascript
gateway.purchase({
  amount: 10.00,
  returnUrl: 'https://example.com/return'
}).then(function (data) {
  // Redirect to payment gateway
  window.location.href = data.redirectUrl;
});
```

Once the payment is complete, the gateway will redirect the user back to the return URL. You can then use the gateway instance to complete the transaction.

```javascript
gateway.completePurchase({
  transactionId: data.transactionId
}).then(function (data) {
  // Payment is complete
});
```

For more information, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use Omnipay with JavaScript?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-with-javascript)