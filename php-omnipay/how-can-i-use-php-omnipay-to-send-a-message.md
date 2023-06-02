# How can I use PHP Omnipay to send a message?
// plain

Using PHP Omnipay, you can send messages to customers in a few different ways.

The first way is to use the `sendMessage()` method. This method takes the customer's email address and a message string as parameters and sends the message to the customer. For example:

```php
$gateway->sendMessage('customer@example.com', 'Hello, this is a message from your store!');
```

The second way is to use the `sendMessageWithTemplate()` method. This method takes the customer's email address, a message template name, and an array of data to be used when rendering the template as parameters. For example:

```php
$gateway->sendMessageWithTemplate('customer@example.com', 'welcome-email', [
    'name' => 'John Smith',
    'store_name' => 'My Store'
]);
```

The third way is to use the `sendMessageWithHtml()` method. This method takes the customer's email address, a subject string, and a HTML string as parameters and sends the message to the customer. For example:

```php
$gateway->sendMessageWithHtml('customer@example.com', 'Welcome to My Store!', '<h1>Hello, John!</h1><p>Welcome to My Store!</p>');
```

Each of these methods returns a boolean value indicating whether the message was sent successfully or not.

## Helpful links
- [PHP Omnipay Documentation](https://omnipay.thephpleague.com/api/message-sending/)

onelinerhub: [How can I use PHP Omnipay to send a message?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-send-a-message)