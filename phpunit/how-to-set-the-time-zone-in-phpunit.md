# How to set the time zone in PHPUnit?
// plain

PHPUnit allows you to set the time zone for your tests using the `phpunit.xml` configuration file.

```
<phpunit>
    <php>
        <ini name="date.timezone" value="Europe/Berlin" />
    </php>
</phpunit>
```

The above example sets the time zone to `Europe/Berlin`.

1. `<phpunit>`: This is the root element of the configuration file.
2. `<php>`: This element contains configuration directives for the PHP interpreter.
3. `<ini>`: This element is used to set configuration directives for the PHP interpreter.
4. `name`: This attribute specifies the name of the configuration directive.
5. `value`: This attribute specifies the value of the configuration directive.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/configuration.html#time-zone)