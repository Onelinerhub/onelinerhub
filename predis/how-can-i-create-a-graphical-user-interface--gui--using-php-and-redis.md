# How can I create a graphical user interface (GUI) using PHP and Redis?
// plain

Creating a graphical user interface (GUI) using PHP and Redis is possible with the help of the Redis extension for PHP. This extension provides an API for communicating with Redis servers from PHP. To create a GUI, you will need to create a basic HTML page with a form that will take user input and store it in Redis.

## Example code

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $redis->hmset('user', array('username' => $username, 'password' => $password));
}
?>
<html>
  <head>
    <title>Login</title>
  </head>
  <body>
    <form action="" method="post">
      <input type="text" name="username" placeholder="Username" />
      <input type="password" name="password" placeholder="Password" />
      <input type="submit" name="submit" value="Submit" />
    </form>
  </body>
</html>
```

The code above creates a basic HTML page with a form that takes user input and stores it in Redis. This form can be used to create a GUI for a Redis-based application.

## Code explanation

1. `$redis = new Redis();` - creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);` - connects to the Redis server on localhost.
3. `if (isset($_POST['submit'])) {` - checks if the form has been submitted.
4. `$username = $_POST['username'];` - gets the username from the form.
5. `$password = $_POST['password'];` - gets the password from the form.
6. `$redis->hmset('user', array('username' => $username, 'password' => $password));` - stores the username and password in Redis.
7. `<form action="" method="post">` - creates a form that will submit data to the server.

## Helpful links
- [Redis extension for PHP](https://github.com/phpredis/phpredis)
- [Creating a GUI with PHP and Redis](https://www.sitepoint.com/creating-a-gui-with-php-and-redis/)

onelinerhub: [How can I create a graphical user interface (GUI) using PHP and Redis?](https://onelinerhub.com/predis/how-can-i-create-a-graphical-user-interface--gui--using-php-and-redis)