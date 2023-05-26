# How to add CC to an email using Swiftmailer?
// plain

Adding CC to an email using Swiftmailer is a simple process.

## Example code

```
$message = (new \Swift_Message('Hello World'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setCc(['cc@domain.org'])
  ->setBody('Here is the message itself')
;
```

The code above will add a CC to the email.

## Code explanation

- \Swift_Message('Hello World') - creates a new Swift_Message object with the subject 'Hello World'
- setFrom(['john@doe.com' => 'John Doe']) - sets the sender of the email
- setTo(['receiver@domain.org', 'other@domain.org' => 'A name']) - sets the primary recipients of the email
- setCc(['cc@domain.org']) - sets the CC recipients of the email
- setBody('Here is the message itself') - sets the body of the email

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to add CC to an email using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-add-cc-to-an-email-using-swiftmailer)