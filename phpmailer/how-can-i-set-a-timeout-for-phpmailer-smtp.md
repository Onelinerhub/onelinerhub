# How can I set a timeout for PHPMailer SMTP?
// plain

The easiest way to set a timeout for PHPMailer SMTP is to use the `setTimeout()` method. This method takes an integer value as an argument, which is the time in seconds.

## Example code

```
//Create a new PHPMailer instance
$mail = new PHPMailer;

//Set timeout
$mail->setTimeout(30);
```

The `setTimeout()` method can also be used to set separate timeouts for the SMTP connection and the SMTP data transfer. To do this, two integer values are passed as arguments, the first being the connection timeout and the second being the data transfer timeout.

## Example code

```
//Create a new PHPMailer instance
$mail = new PHPMailer;

//Set timeout
$mail->setTimeout(20, 10);
```

This sets the SMTP connection timeout to 20 seconds and the SMTP data transfer timeout to 10 seconds.

It is also possible to set the timeout for the SMTP connection using the `SMTPOptions` property. This property takes an array of options as an argument. The `timeout` key in the array sets the timeout for the SMTP connection.

## Example code

```
//Create a new PHPMailer instance
$mail = new PHPMailer;

//Set timeout
$mail->SMTPOptions = array(
    'timeout' => 30
);
```

This sets the SMTP connection timeout to 30 seconds.

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How can I set a timeout for PHPMailer SMTP?](https://onelinerhub.com/phpmailer/how-can-i-set-a-timeout-for-phpmailer-smtp)