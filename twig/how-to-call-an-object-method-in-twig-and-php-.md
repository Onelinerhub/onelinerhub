# How to call an object method in Twig and PHP?
// plain

Twig and PHP are two popular web development languages. To call an object method in Twig and PHP, you can use the `{{ object.method() }}` syntax. For example,

```
{% set myObject = {
  'name': 'John',
  'sayName': function() {
    return this.name;
  }
} %}

{{ myObject.sayName() }}
```

This will output `John`.

The code consists of the following parts:

1. `{% set myObject = { ... } %}` - This creates an object with a `name` property and a `sayName` method.
2. `{{ myObject.sayName() }}` - This calls the `sayName` method on the `myObject` object.

For more information, see the [Twig documentation](https://twig.symfony.com/doc/2.x/templates.html#other-operators) and the [PHP documentation](https://www.php.net/manual/en/language.oop5.basic.php).

onelinerhub: [How to call an object method in Twig and PHP?](https://onelinerhub.com/twig/how-to-call-an-object-method-in-twig-and-php-)