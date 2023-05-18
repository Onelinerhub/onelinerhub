# How to use body_class() in WordPress with PHP?
// plain

The `body_class()` function in WordPress is used to add custom classes to the `<body>` element of a WordPress page. This can be used to target specific pages or elements with custom CSS.

## Example code

```
<body <?php body_class(); ?>>
```

## Output example

```
<body class="home page-template page-template-page-templates page-template-full-width page-template-page-templatesfull-width-php page page-id-2 logged-in admin-bar no-customize-support">
```

## Code explanation

- `body_class()`: This is the function that adds the classes to the `<body>` element.
- `<body>`: This is the HTML element that the classes are added to.
- `home`: This is an example of a class that is added to the `<body>` element.

## Helpful links
- [WordPress Codex - body_class()](https://codex.wordpress.org/Function_Reference/body_class)

onelinerhub: [How to use body_class() in WordPress with PHP?](https://onelinerhub.com/php-wordpress/how-to-use-body_class---in-wordpress-with-php)