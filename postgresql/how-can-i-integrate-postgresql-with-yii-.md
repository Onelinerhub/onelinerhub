# How can I integrate PostgreSQL with Yii2?
// plain

PostgreSQL can be integrated with Yii2 by using the PostgreSQL Extension for Yii2. This extension provides a PostgreSQL database driver and schema migration tool for Yii2 applications. To use the extension, first install it using Composer:

```
composer require yiisoft/yii2-postgres
```

Once the extension is installed, you can configure the database connection in the application configuration file:

```
'components' => [
    'db' => [
        'class' => 'yii\db\Connection',
        'dsn' => 'pgsql:host=localhost;dbname=mydatabase',
        'username' => 'myuser',
        'password' => 'mypassword',
    ],
    // ...
],
```

## Code explanation


- `yiisoft/yii2-postgres` - The PostgreSQL Extension for Yii2.
- `yii\db\Connection` - The class that represents the database connection.
- `pgsql:host=localhost;dbname=mydatabase` - The DSN (Data Source Name) used to connect to the database.
- `myuser` - The username used to connect to the database.
- `mypassword` - The password used to connect to the database.

For more information, see the [PostgreSQL Extension for Yii2 documentation](https://github.com/yiisoft/yii2-postgres).

onelinerhub: [How can I integrate PostgreSQL with Yii2?](https://onelinerhub.com/postgresql/how-can-i-integrate-postgresql-with-yii-)