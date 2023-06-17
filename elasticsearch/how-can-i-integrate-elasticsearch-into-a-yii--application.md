# How can I integrate Elasticsearch into a Yii2 application?
// plain

Integrating Elasticsearch into a Yii2 application is a straightforward process. The following steps will help you get started:

1. Install the [elasticsearch-php](https://github.com/elastic/elasticsearch-php) library:

```
composer require elasticsearch/elasticsearch
```

2. Create a new component in your Yii2 application's `config/main.php` file:

```
'components' => [
  ...
  'elasticsearch' => [
    'class' => 'yii\elasticsearch\Connection',
    'nodes' => [
      ['http_address' => '127.0.0.1:9200'],
    ],
  ],
  ...
],
```

3. Create a `Search` model class in your application that extends `yii\elasticsearch\ActiveRecord`:

```
<?php

namespace app\models;

use yii\elasticsearch\ActiveRecord;

class Search extends ActiveRecord
{
    public function attributes()
    {
        return ['title', 'content'];
    }
}
```

4. Create an action in the controller to perform the search:

```
public function actionSearch()
{
    $query = Yii::$app->request->get('query');
    $results = Search::find()->query([
        'multi_match' => [
            'query' => $query,
            'fields' => ['title', 'content']
        ]
    ])->all();

    return $this->render('search', [
        'results' => $results
    ]);
}
```

5. Create a view file to render the search results:

```
<?php foreach ($results as $result): ?>
    <h2><?= $result->title ?></h2>
    <p><?= $result->content ?></p>
<?php endforeach; ?>
```

These steps should get you up and running with Elasticsearch in your Yii2 application.

For more information, please refer to the official [Elasticsearch Yii2 extension](https://github.com/yiisoft/yii2-elasticsearch) documentation.

onelinerhub: [How can I integrate Elasticsearch into a Yii2 application?](https://onelinerhub.com/elasticsearch/how-can-i-integrate-elasticsearch-into-a-yii--application)