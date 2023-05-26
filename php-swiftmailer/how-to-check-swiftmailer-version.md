# How to check Swiftmailer version?
// plain

To check the version of Swiftmailer, you can use the following code:
```
$swiftmailerVersion = \Swift_DependencyContainer::getInstance()->lookup('transport.version');
echo $swiftmailerVersion;
```
This will output the version of Swiftmailer, for example: `6.2.3`.

The code consists of two parts:
1. `\Swift_DependencyContainer::getInstance()->lookup('transport.version')` - This part looks up the version of the transport layer of Swiftmailer.
2. `echo $swiftmailerVersion` - This part prints out the version of Swiftmailer.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to check Swiftmailer version?](https://onelinerhub.com/php-swiftmailer/how-to-check-swiftmailer-version)