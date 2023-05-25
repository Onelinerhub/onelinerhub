# How to run PHPUnit in a Docker container?
// plain

1. Install the PHPUnit package in the Docker container:
```
docker-compose exec php composer require --dev phpunit/phpunit
```

2. Create a `phpunit.xml` configuration file in the project root directory.

3. Run the PHPUnit tests in the Docker container:
```
docker-compose exec php ./vendor/bin/phpunit
```

4. The output of the tests will be displayed in the terminal.

5. For more information, please refer to the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [How to run PHPUnit in a Docker container?](https://onelinerhub.com/phpunit/how-to-run-phpunit-in-a-docker-container)