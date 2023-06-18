# How do I integrate Sphinxsearch with Yii2?
// plain

Integrating Sphinxsearch with Yii2 is fairly simple and can be done in a few steps.

1. Install the [sphinx-yii2](https://github.com/SpiralOut/sphinx-yii2) extension.

2. Configure the extension in the `config/web.php` file:

```php
'sphinx' => [
    'class' => 'yii\sphinx\Connection',
    'dsn' => 'mysql:host=127.0.0.1;port=9306;',
    'username' => '',
    'password' => '',
],
```

3. Create a model that extends `yii\sphinx\ActiveRecord` and define your searchable attributes:

```php
class MyModel extends \yii\sphinx\ActiveRecord
{
    public function attributes()
    {
        return ['id', 'title', 'description'];
    }
}
```

4. Create a search query using the model:

```php
$query = MyModel::find()
    ->match('title', 'My Title')
    ->all();
```

5. Execute the query and get the results:

```php
$results = $query->all();

foreach ($results as $result) {
    echo $result->title;
}
```

This is the basic workflow for integrating Sphinxsearch with Yii2. For more information, please see the [sphinx-yii2](https://github.com/SpiralOut/sphinx-yii2) extension documentation.

onelinerhub: [How do I integrate Sphinxsearch with Yii2?](https://onelinerhub.com/sphinxsearch/how-do-i-integrate-sphinxsearch-with-yii-)