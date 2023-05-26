# How to mock SwiftMailer?
// plain

Mocking SwiftMailer can be done using a library such as Mockery. Mockery is a simple yet flexible PHP mock object framework for use in unit testing with PHPUnit, PHPSpec or any other testing framework.

## Example code

```
$mock = \Mockery::mock('Swift_Mailer');
$mock->shouldReceive('send')
    ->once()
    ->andReturn(true);
```

## Output example

```
true
```

## Code explanation

- `$mock = \Mockery::mock('Swift_Mailer');` - creates a mock object of the Swift_Mailer class
- `$mock->shouldReceive('send')` - sets up an expectation that the `send` method will be called
- `->once()` - sets the expectation that the `send` method will be called only once
- `->andReturn(true)` - sets the expectation that the `send` method will return `true`

## Helpful links
- [Mockery](https://github.com/mockery/mockery)
- [PHPUnit](https://phpunit.de/)
- [PHPSpec](http://www.phpspec.net/)

onelinerhub: [How to mock SwiftMailer?](https://onelinerhub.com/php-swiftmailer/how-to-mock-swiftmailer)