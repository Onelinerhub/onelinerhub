# How do I use the list-unsubscribe feature in PHPMailer?
// plain

The `list-unsubscribe` feature in PHPMailer is a way to provide an automated method for users to unsubscribe from emails. It allows users to easily unsubscribe from a mailing list without having to contact the sender. Here's an example of how to use it:

```php
$mail = new PHPMailer;
$mail->addCustomHeader('List-Unsubscribe', '<http://example.com/unsubscribe.php>');
```

This code will add a `List-Unsubscribe` header to the email that contains a link to an unsubscribe page. When the user clicks on the link, they will be taken to the unsubscribe page where they can unsubscribe from the mailing list.

The code consists of two parts:

1. `$mail = new PHPMailer;` - This creates a new instance of the PHPMailer class.
2. `$mail->addCustomHeader('List-Unsubscribe', '<http://example.com/unsubscribe.php>');` - This adds a custom header to the email containing a link to the unsubscribe page.

For more information on the `list-unsubscribe` feature in PHPMailer, see the [documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial:-Using-the-List-Unsubscribe-Header).

onelinerhub: [How do I use the list-unsubscribe feature in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-use-the-list-unsubscribe-feature-in-phpmailer)