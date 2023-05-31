# How to integrate Twig with Yii2?
// plain

Twig is a templating language for PHP which can be used to integrate with Yii2. It is easy to install and use Twig with Yii2.

## Example code

```
$config = [
    'class' => 'yii\twig\ViewRenderer',
    'cachePath' => '@runtime/Twig/cache',
    // Array of twig options:
    'options' => [
        'auto_reload' => true,
    ],
    'globals' => [
        'html' => ['class' => '\yii\helpers\Html'],
    ],
    'uses' => ['yii\bootstrap'],
];
```

This code configures the Twig view renderer for Yii2. It sets the cache path, options, globals and uses.

## Helpful links
- [Twig for Yii2](https://github.com/yiisoft/yii2-twig)
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to integrate Twig with Yii2?](https://onelinerhub.com/twig/how-to-integrate-twig-with-yii2-)