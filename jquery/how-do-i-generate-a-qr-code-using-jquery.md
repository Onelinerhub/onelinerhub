# How do I generate a QR code using jQuery?
// plain

Generating a QR code using jQuery is easy and straightforward. To do so, you need to use an external library such as [jQuery.qrcode](https://larsjung.de/jquery-qrcode/).

Here is an example code to generate a QR code with `jQuery.qrcode`:

```javascript
$('#qrcode').qrcode({
    text: "http://example.com"
});
```

This will generate a QR code with the text "http://example.com".

The code consists of the following parts:

* `$('#qrcode')` - This is a jQuery selector that selects the element with the id `qrcode`.
* `.qrcode()` - This is the jQuery.qrcode function that creates the QR code.
* `{ text: "http://example.com" }` - This is an object that contains the text to be encoded in the QR code.

For more information, see the [jQuery.qrcode documentation](https://larsjung.de/jquery-qrcode/).

onelinerhub: [How do I generate a QR code using jQuery?](https://onelinerhub.com/jquery/how-do-i-generate-a-qr-code-using-jquery)