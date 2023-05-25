# How to set environment variables for PHPUnit?
// plain

Environment variables can be set for PHPUnit by using the `phpunit.xml` configuration file.

```
<phpunit>
    <php>
        <env name="VARIABLE_NAME" value="VARIABLE_VALUE"/>
    </php>
</phpunit>
```

The above code block sets the environment variable `VARIABLE_NAME` to `VARIABLE_VALUE`.

1. `<phpunit>`: This is the root element of the configuration file.
2. `<php>`: This element contains configuration directives for PHP.
3. `<env>`: This element sets environment variables.
4. `name`: This attribute sets the name of the environment variable.
5. `value`: This attribute sets the value of the environment variable.

## Helpful links

- [PHPUnit Documentation - Configuration](https://phpunit.readthedocs.io/en/9.2/configuration.html)

onelinerhub: [How to set environment variables for PHPUnit?](https://onelinerhub.com/phpunit/how-to-set-environment-variables-for-phpunit)