# How can I debug an issue with PHP Omnipay?
// plain

Debugging an issue with PHP Omnipay can be done in several ways.

Firstly, you can use the `dump()` method to inspect the data that is being processed. This method will output the data in an easy to read format. For example:

```php
$data = $gateway->purchase($params)->send();
$data->dump();
```

The output of this command will look something like this:

```
Array
(
    [status] => success
    [message] => Payment successful
    [data] => Array
        (
            [transaction_id] => 12345
            [amount] => 10.00
            [currency] => USD
        )

)
```

Secondly, you can enable logging in order to get more detailed information about what is happening. This can be done by setting the `log` parameter to `true` when creating the gateway instance:

```php
$gateway = Omnipay::create('MyGateway', [
    'log' => true,
]);
```

This will create a log file in the `logs` directory of your project. The log file will contain detailed information about all the requests and responses that are being sent and received.

Finally, you can also use the `debug` method to inspect the raw request and response data. This method will output the raw data in an easy to read format. For example:

```php
$data = $gateway->purchase($params)->send();
$data->debug();
```

The output of this command will look something like this:

```
Request:
POST /payment HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "amount": 10.00,
    "currency": "USD"
}

Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "message": "Payment successful",
    "data": {
        "transaction_id": "12345",
        "amount": 10.00,
        "currency": "USD"
    }
}
```

These are the three main ways to debug an issue with PHP Omnipay.

For more information, please refer to the [official documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How can I debug an issue with PHP Omnipay?](https://onelinerhub.com/php-omnipay/how-can-i-debug-an-issue-with-php-omnipay)