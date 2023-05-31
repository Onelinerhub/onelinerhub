# How to use yield in Twig with PHP?
// plain

Yield in Twig with PHP can be used to create a template that can be reused in multiple places. It allows you to create a template that can be used to render a specific part of a page.

## Example code

```
{% set my_template = '<div>{{ content }}</div>' %}

{% macro my_macro(content) %}
    {{ my_template|format(content=content) }}
{% endmacro %}

{{ my_macro('Hello World!') }}
```

## Output example

```
<div>Hello World!</div>
```

## Code explanation

- `{% set my_template = '<div>{{ content }}</div>' %}`: This sets a variable called `my_template` to a string containing a template.
- `{% macro my_macro(content) %}`: This defines a macro called `my_macro` which takes a parameter called `content`.
- `{{ my_template|format(content=content) }}`: This uses the `format` filter to render the `my_template` variable with the `content` parameter passed to the macro.
- `{{ my_macro('Hello World!') }}`: This calls the `my_macro` macro with the string `Hello World!` as the `content` parameter.

## Helpful links
- [Twig Documentation - Macros](https://twig.symfony.com/doc/2.x/tags/macro.html)
- [Twig Documentation - Filters](https://twig.symfony.com/doc/2.x/filters/index.html)

onelinerhub: [How to use yield in Twig with PHP?](https://onelinerhub.com/twig/how-to-use-yield-in-twig-with-php-)