# How do I remove an address from PHPMailer?
// plain

To remove an address from PHPMailer, you can use the `removeAddress()` method. This method takes two parameters, the first being the address to remove, and the second being the type of the address (`to`, `cc`, or `bcc`).

For example:
```
$mail->removeAddress('example@example.com', 'to');
```

The `removeAddress()` method returns `true` if the address was successfully removed, or `false` if it was not.

The parts of the code are:
- `removeAddress()`: This is the method used to remove an address from PHPMailer.
- `example@example.com`: This is the address to be removed.
- `to`: This is the type of address being removed.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I remove an address from PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-remove-an-address-from-phpmailer)