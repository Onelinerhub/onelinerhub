# How do I use the PHP Omnipay Validator?
// plain

The PHP Omnipay Validator is a library that allows developers to validate credit card numbers, expiration dates, and other details related to payments. It is built on top of the Omnipay library and can be used to validate payment details before submitting a payment request.

To use the PHP Omnipay Validator, you need to first install the library and include it in your project.

```
composer require omnipay/validator
```

Then you can create a new Validator instance, passing in the payment details as an array:

```
$validator = new Omnipay\Validator\Validator($paymentDetails);
```

You can then validate the payment details by calling the `validate` method:

```
$validator->validate();
```

If the payment details are valid, the `validate` method will return `true`; otherwise it will return `false`.

You can also access the validation errors by calling the `getErrors` method:

```
$errors = $validator->getErrors();
```

The `getErrors` method will return an array of validation errors, if any.

For more information, please refer to the [PHP Omnipay Validator documentation](https://github.com/thephpleague/omnipay-validator).

onelinerhub: [How do I use the PHP Omnipay Validator?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-php-omnipay-validator)