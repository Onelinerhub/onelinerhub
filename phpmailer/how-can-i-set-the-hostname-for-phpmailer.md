# How can I set the hostname for PHPMailer?
// plain

PHPMailer is a library for sending emails from PHP. Setting the hostname is an important step when using PHPMailer to send emails.

To set the hostname for PHPMailer, you can use the `$mail->Host` property. The `$mail` variable should be a PHPMailer object.

For example,

```
$mail->Host = 'smtp.example.com';
```

This will set the hostname to `smtp.example.com` for the PHPMailer object.

You can also set the hostname as an array of hosts, in which case PHPMailer will try each host in turn until it finds one that works.

For example,

```
$mail->Host = array('smtp1.example.com','smtp2.example.com');
```

This will set the hostname as an array of two hosts, `smtp1.example.com` and `smtp2.example.com`.

You can also set the hostname to an IP address. For example,

```
$mail->Host = '127.0.0.1';
```

This will set the hostname to the IP address `127.0.0.1`.

For more information on setting the hostname for PHPMailer, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How can I set the hostname for PHPMailer?](https://onelinerhub.com/phpmailer/how-can-i-set-the-hostname-for-phpmailer)