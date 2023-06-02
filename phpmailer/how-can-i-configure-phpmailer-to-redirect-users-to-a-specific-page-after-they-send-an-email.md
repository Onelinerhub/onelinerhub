# How can I configure PHPMailer to redirect users to a specific page after they send an email?
// plain

To configure PHPMailer to redirect users to a specific page after they send an email, you can use the `header()` function in the `onAfterSend()` event. Here is an example:

```
$mail = new PHPMailer;
$mail->onAfterSend(function($mail) {
    header("Location: http://www.example.com/thankyou.html");
});
```

This code will redirect the user to the `thankyou.html` page after they send the email.

## Code explanation

- `$mail = new PHPMailer;`: creates a new instance of the PHPMailer class.
- `onAfterSend()`: is an event that is triggered after the email is sent.
- `function($mail)`: defines the function to be executed when the event is triggered.
- `header()`: is a PHP function used to send a raw HTTP header.
- `Location:`: is the header name that specifies the redirect URL.

Here are some relevant links for further reading:
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [PHP header() Function](https://www.w3schools.com/php/func_network_header.asp)

onelinerhub: [How can I configure PHPMailer to redirect users to a specific page after they send an email?](https://onelinerhub.com/phpmailer/how-can-i-configure-phpmailer-to-redirect-users-to-a-specific-page-after-they-send-an-email)