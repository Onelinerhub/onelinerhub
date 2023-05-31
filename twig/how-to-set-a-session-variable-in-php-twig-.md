# How to set a session variable in PHP Twig?
// plain

Session variables can be set in PHP Twig using the `set_attribute` function.

```
<?php
$session->set_attribute('name', 'value');
```

This will set the session variable `name` to the value `value`.

## Code explanation


1. `$session` - an instance of the `Twig_Session` class
2. `set_attribute` - a function of the `Twig_Session` class that sets a session variable
3. `name` - the name of the session variable
4. `value` - the value of the session variable

## Helpful links

1. [Twig Documentation](https://twig.symfony.com/doc/2.x/)
2. [Twig Session Class](https://twig.symfony.com/api/2.x/Twig_Session.html)

onelinerhub: [How to set a session variable in PHP Twig?](https://onelinerhub.com/twig/how-to-set-a-session-variable-in-php-twig-)