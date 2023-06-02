# How do I use PHPMailer with reCAPTCHA?
// plain

Using PHPMailer with reCAPTCHA is simple. To start, you need to create a [reCAPTCHA](https://www.google.com/recaptcha/admin) account and get a site key and secret key. Then, you need to include the reCAPTCHA PHP library in your script.

```php
require_once('recaptchalib.php');
$siteKey = "YOUR_SITE_KEY";
$secret = "YOUR_SECRET_KEY";
```

Next, you need to create a HTML form with the reCAPTCHA widget.

```html
<form action="verify.php" method="POST">
  <div class="g-recaptcha" data-sitekey="<?php echo $siteKey; ?>"></div>
  <input type="submit" value="Submit">
</form>
```

Then, in the `verify.php` file, you need to verify the reCAPTCHA response.

```php
$response = $_POST['g-recaptcha-response'];
$remoteIp = $_SERVER['REMOTE_ADDR'];
$reCaptchaValidation = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=$secret&response=$response&remoteip=$remoteIp");
$result = json_decode($reCaptchaValidation);

if ($result->success) {
  // reCAPTCHA was successful
  // Send the email using PHPMailer
  // ...
} else {
  // reCAPTCHA was unsuccessful
  // Show an error message
  // ...
}
```

Finally, you can use PHPMailer to send the email.

```php
$mail = new PHPMailer;
$mail->setFrom('from@example.com', 'Your Name');
$mail->addAddress('to@example.com', 'Recipient Name');
$mail->Subject = 'PHPMailer + reCAPTCHA Test';
$mail->Body = 'This is a test message from PHPMailer + reCAPTCHA!';

if (!$mail->send()) {
  echo 'Message could not be sent.';
  echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
  echo 'Message has been sent';
}
```

## Output example

```
Message has been sent
```

## Helpful links
- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [reCAPTCHA](https://www.google.com/recaptcha/intro/v3.html)

onelinerhub: [How do I use PHPMailer with reCAPTCHA?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-recaptcha)