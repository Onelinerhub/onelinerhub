# payment

How do I delete a payment using PHP Omnipay?
// plain

To delete a payment using PHP Omnipay, you can use the `deleteCard()` method. The method requires an argument of type `CreditCard` object. The following example code snippet shows how to delete a payment using PHP Omnipay:

```
$card = new CreditCard($cardDetails);
$response = $gateway->deleteCard($card)->send();
if ($response->isSuccessful()) {
    echo 'The payment was deleted successfully!';
}
```

The `deleteCard()` method returns an instance of the `ResponseInterface` object. You can use the `isSuccessful()` method to check if the payment was deleted successfully or not.

## Code explanation


* `CreditCard` - This is the class used to create a `CreditCard` object.
* `$cardDetails` - This is an array of credit card details used to create a `CreditCard` object.
* `$gateway` - This is an instance of the `Gateway` class.
* `deleteCard()` - This is the method used to delete a payment.
* `send()` - This is the method used to send the request.
* `isSuccessful()` - This is the method used to check if the response was successful or not.

## Helpful links

* [PHP Omnipay Documentation](https://github.com/thephpleague/omnipay)
* [CreditCard Class](https://github.com/thephpleague/omnipay/blob/master/src/CreditCard.php)
* [Gateway Class](https://github.com/thephpleague/omnipay/blob/master/src/Gateway.php)
* [ResponseInterface Class](https://github.com/thephpleague/omnipay/blob/master/src/ResponseInterface.php)

onelinerhub: [payment

How do I delete a payment using PHP Omnipay?](https://onelinerhub.com/php-omnipay/payment--how-do-i-delete-a-payment-using-php-omnipay)