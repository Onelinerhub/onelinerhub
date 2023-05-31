# How to create a template in PHP Twig?
// plain

Creating a template in PHP Twig is a simple process.

```
{% extends "base.html" %}

{% block title %}My Page{% endblock %}

{% block body %}
    <h1>My Page</h1>
    <p>Welcome to my page!</p>
{% endblock %}
```

This example code will create a template that extends the base.html template, and adds a title and body block. The title block will contain the text "My Page", and the body block will contain an h1 tag with the text "My Page" and a paragraph tag with the text "Welcome to my page!".

1. `{% extends "base.html" %}` - This line tells Twig to extend the base.html template.
2. `{% block title %}My Page{% endblock %}` - This line creates a title block with the text "My Page".
3. `{% block body %}` - This line creates a body block.
4. `<h1>My Page</h1>` - This line adds an h1 tag with the text "My Page" to the body block.
5. `<p>Welcome to my page!</p>` - This line adds a paragraph tag with the text "Welcome to my page!" to the body block.
6. `{% endblock %}` - This line ends the body block.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to create a template in PHP Twig?](https://onelinerhub.com/twig/how-to-create-a-template-in-php-twig-)