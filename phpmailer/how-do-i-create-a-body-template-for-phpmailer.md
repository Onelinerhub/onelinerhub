# How do I create a body template for PHPMailer?
// plain

Creating a body template for PHPMailer is quite easy. You just need to use the `$mail->Body` property of the PHPMailer class. This property is used to set the body of the email.

## Example code

```
$mail = new PHPMailer();
$mail->Body = 'This is the body of the email';
```

The `$mail->Body` property accepts a string, so you can use HTML and CSS to format the email body. You can also use variables in the string to make the body dynamic.

## Example code

```
$name = 'John Doe';
$mail = new PHPMailer();
$mail->Body = 'Hello, <b>$name</b>, welcome to our website!';
```

## Output example


Hello, **John Doe**, welcome to our website!

## Code explanation


1. `$mail = new PHPMailer();` - This line creates a new instance of the PHPMailer class.
2. `$mail->Body = 'This is the body of the email';` - This line sets the body of the email.
3. `$name = 'John Doe';` - This line creates a variable for the name.
4. `$mail->Body = 'Hello, <b>$name</b>, welcome to our website!';` - This line sets the body of the email using the variable for the name.

## Helpful links

- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How do I create a body template for PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-create-a-body-template-for-phpmailer)