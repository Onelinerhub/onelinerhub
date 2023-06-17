# How can I use JQuery with Yii2?
// plain

### Using JQuery with Yii2

Yii2 is a PHP framework that supports JQuery. To use JQuery in Yii2, you need to include the JQuery library in the application. This can be done by adding the following code to the `Asset` configuration in the `AppAsset.php` file:

```php
public $js = [
    'js/jquery.js',
];
```

Once the JQuery library is included, you can use it in your application. For example, the following code will select all `<p>` elements and add a class `my-class` to them:

```js
$('p').addClass('my-class');
```

## Code explanation

- `$('p')`: This is a JQuery selector that selects all `<p>` elements.
- `addClass('my-class')`: This is a JQuery method that adds the class `my-class` to the selected elements.

For further information about using JQuery with Yii2, please refer to the following links:
- [Yii2 JQuery](https://www.yiiframework.com/doc/guide/2.0/en/output-jquery)
- [JQuery API Documentation](https://api.jquery.com/)

onelinerhub: [How can I use JQuery with Yii2?](https://onelinerhub.com/jquery/how-can-i-use-jquery-with-yii-)