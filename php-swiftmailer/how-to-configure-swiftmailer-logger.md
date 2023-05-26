# How to configure Swiftmailer logger?
// plain

Swiftmailer logger can be configured to log emails sent by the application.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Create the logger
$logger = new Swift_Plugins_Loggers_ArrayLogger();

// Register the logger
$mailer->registerPlugin(new Swift_Plugins_LoggerPlugin($logger));

// Send the message
$result = $mailer->send($message);

// Dump the log
echo $logger->dump();
```

## Output example

```
== START LOGGING ==
Sending message to: recipient@example.org

<<< 220 smtp.example.org ESMTP
>>> EHLO localhost
<<< 250-smtp.example.org
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-AUTH PLAIN LOGIN
250-AUTH=PLAIN LOGIN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
>>> STARTTLS
<<< 220 2.0.0 Ready to start TLS
>>> EHLO localhost
<<< 250-smtp.example.org
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-AUTH PLAIN LOGIN
250-AUTH=PLAIN LOGIN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
>>> AUTH LOGIN
<<< 334 VXNlcm5hbWU6
>>> <credentials hidden>
<<< 334 UGFzc3dvcmQ6
>>> <credentials hidden>
<<< 235 2.7.0 Authentication successful
>>> MAIL FROM:<from@example.org>
<<< 250 2.1.0 Ok
>>> RCPT TO:<recipient@example.org>
<<< 250 2.1.5 Ok
>>> DATA
<<< 354 End data with <CR><LF>.<CR><LF>
>>> Date: Mon, 13 Jul 2020 15:00:00 +0200
>>> To: recipient@example.org
>>> Subject: Test
>>>
>>> This is a test
>>>
>>> .
<<< 250 2.0.0 Ok: queued as 12345
== END LOGGING ==
```

## Code explanation


1. Create the Transport - This creates the transport layer for the mailer.
2. Create the Mailer - This creates the mailer using the transport layer.
3. Create the logger - This creates the logger for the mailer.
4. Register the logger - This registers the logger with the mailer.
5. Send the message - This sends the message using the mailer.
6. Dump the log - This dumps the log of the mailer.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swiftmailer Logger Plugin](https://swiftmailer.symfony.com/docs/plugins.html#logging)

onelinerhub: [How to configure Swiftmailer logger?](https://onelinerhub.com/php-swiftmailer/how-to-configure-swiftmailer-logger)