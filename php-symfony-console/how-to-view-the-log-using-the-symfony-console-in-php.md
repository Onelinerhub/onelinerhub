# How to view the log using the Symfony console in PHP?
// plain

The Symfony console in PHP can be used to view the log. To do this, the `tail` command can be used. This command will display the last 10 lines of the log file by default.

```
$ php bin/console tail
```

The output of this command will look something like this:
```
[2020-04-20 10:45:12] request.INFO: Matched route "homepage". {"route":"homepage","route_parameters":{"_controller":"App\\Controller\\HomeController::index","_route":"homepage"},"request_uri":"http://localhost:8000/","method":"GET"} []
[2020-04-20 10:45:12] security.INFO: Populated the TokenStorage with an anonymous Token. [] []
[2020-04-20 10:45:12] request.INFO: Matched route "_wdt". {"route":"_wdt","route_parameters":{"_controller":"web_profiler.controller.profiler::toolbarAction","token":"f9f9f9","_route":"_wdt"},"request_uri":"http://localhost:8000/_wdt/f9f9f9","method":"GET"} []
```

The `tail` command can also be used with the `-f` flag to follow the log file and display new lines as they are written.

```
$ php bin/console tail -f
```

The `tail` command also accepts a `-n` flag to specify the number of lines to display.

```
$ php bin/console tail -n 20
```

## Helpful links
- [Symfony Console Documentation](https://symfony.com/doc/current/console.html)

onelinerhub: [How to view the log using the Symfony console in PHP?](https://onelinerhub.com/php-symfony-console/how-to-view-the-log-using-the-symfony-console-in-php)