# How to use Markdown with Twig and PHP?
// plain

Markdown is a lightweight markup language that can be used to format text. It can be used with Twig and PHP to create dynamic webpages.

## Example code

```
<?php
$twig = new Twig_Environment();
$template = $twig->loadTemplate('template.html');
echo $template->render(array('content' => Markdown::parse($content)));
?>
```

## Output example

```
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>My Page</h1>
    <p>This is my page.</p>
  </body>
</html>
```

## Code explanation

- `$twig = new Twig_Environment();`: This creates a new Twig environment.
- `$template = $twig->loadTemplate('template.html');`: This loads the template file.
- `echo $template->render(array('content' => Markdown::parse($content)));`: This renders the template with the parsed Markdown content.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Markdown Documentation](https://daringfireball.net/projects/markdown/)

onelinerhub: [How to use Markdown with Twig and PHP?](https://onelinerhub.com/twig/how-to-use-markdown-with-twig-and-php-)