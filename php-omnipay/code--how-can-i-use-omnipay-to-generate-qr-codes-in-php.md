# code

How can I use Omnipay to generate QR codes in PHP?
// plain

Omnipay is a payment processing library for PHP that makes it easy to integrate payment gateways into web applications. It can be used to generate QR codes in PHP with the help of the [Barcode Generator Plugin](https://github.com/thephpleague/omnipay-barcode-generator).

Example code block:
```
$gateway = Omnipay::create('BarcodeGenerator');
$gateway->setAmount('10.00');
$gateway->setCurrency('USD');
$response = $gateway->purchase();
$qrCode = $response->getQrCode();
```

## Code explanation


- `$gateway = Omnipay::create('BarcodeGenerator')`: creates a new instance of the BarcodeGenerator gateway.
- `$gateway->setAmount('10.00')`: sets the amount of the transaction.
- `$gateway->setCurrency('USD')`: sets the currency of the transaction.
- `$response = $gateway->purchase()`: sends the transaction to the gateway and gets the response.
- `$qrCode = $response->getQrCode()`: gets the QR code object from the response.

The output of the example code will be a QR code object which can be used to display the QR code in a web page.

## Helpful links
- [Omnipay](https://omnipay.thephpleague.com/)
- [Barcode Generator Plugin](https://github.com/thephpleague/omnipay-barcode-generator)

onelinerhub: [code

How can I use Omnipay to generate QR codes in PHP?](https://onelinerhub.com/php-omnipay/code--how-can-i-use-omnipay-to-generate-qr-codes-in-php)