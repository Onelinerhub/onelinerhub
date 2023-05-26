# How to access Swiftmailer logs?
// plain

Swiftmailer logs can be accessed by using the `Swift_Plugins_Loggers_ArrayLogger` class. This class allows you to log messages and errors that occur during the sending of emails.

## Example code

```
$logger = new Swift_Plugins_Loggers_ArrayLogger();
$mailer->registerPlugin(new Swift_Plugins_LoggerPlugin($logger));
```

## Output example

```
Array
(
)
```

The code above registers the logger plugin with the mailer. After sending the email, the log messages can be accessed using the `getMessages()` method of the `ArrayLogger` class.

## Example code

```
$logs = $logger->getMessages();
```

## Output example

```
Array
(
    [0] => Connection could not be established with host smtp.example.com [Connection timed out #110]
    [1] => Connection could not be established with host smtp.example.com [Connection timed out #110]
    [2] => Connection could not be established with host smtp.example.com [Connection timed out #110]
    [3] => Connection could not be established with host smtp.example.com [Connection timed out #110]
    [4] => Connection could not be established with host smtp.example.com [Connection timed out #110]
)
```

The `getMessages()` method returns an array of log messages. These messages can be used to debug any issues that may have occurred during the sending of emails.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift_Plugins_Loggers_ArrayLogger Class](https://swiftmailer.symfony.com/api/master/class-Swift_Plugins_Loggers_ArrayLogger.html)

onelinerhub: [How to access Swiftmailer logs?](https://onelinerhub.com/php-swiftmailer/how-to-access-swiftmailer-logs)