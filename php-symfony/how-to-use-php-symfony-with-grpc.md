# How to use PHP Symfony with gRPC?
// plain

Using PHP Symfony with gRPC is relatively straightforward.

First, install the gRPC PHP extension:
```
$ pecl install grpc
```

Then, add the following line to your `php.ini` file:
```
extension=grpc.so
```

Next, create a Symfony project and install the gRPC bundle:
```
$ composer create-project symfony/skeleton my_project
$ cd my_project
$ composer require grpc/grpc
```

Finally, create a gRPC client and server:
```
$ bin/console make:grpc:client
$ bin/console make:grpc:server
```

You can now use the generated client and server to communicate with each other using gRPC.

## Helpful links
- [gRPC PHP Extension](https://pecl.php.net/package/grpc)
- [gRPC Bundle for Symfony](https://github.com/grpc/grpc-symfony-bundle)

onelinerhub: [How to use PHP Symfony with gRPC?](https://onelinerhub.com/php-symfony/how-to-use-php-symfony-with-grpc)