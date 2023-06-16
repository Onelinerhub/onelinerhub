# How do I use Docker Compose to deploy a Laravel application in PHP?
// plain

To deploy a Laravel application in PHP using Docker Compose, follow these steps:

1. Create a `docker-compose.yml` file in the root of your Laravel application.

```
version: '3'
services:
  web:
    build: .
    ports:
      - "80:80"
    volumes:
      - ./:/var/www/html
    links:
      - mysql
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: laravel
```

2. Run the `docker-compose up -d` command to start the containers in detached mode.

```
$ docker-compose up -d
Creating network "laravel_default" with the default driver
Creating laravel_web_1 ... done
Creating laravel_mysql_1 ... done
```

3. Install the dependencies for the application with `docker-compose exec web composer install`.

```
$ docker-compose exec web composer install
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 11 installs, 0 updates, 0 removals
  - Installing symfony/psr-http-message-bridge (v1.2.0): Downloading (100%)
  - Installing symfony/http-foundation (v4.4.9): Downloading (100%)
  - Installing symfony/http-kernel (v4.4.9): Downloading (100%)
  - Installing psr/http-message (1.0.1): Downloading (100%)
  - Installing psr/container (1.0.0): Downloading (100%)
  - Installing symfony/event-dispatcher (v4.4.9): Downloading (100%)
  - Installing symfony/debug (v4.4.9): Downloading (100%)
  - Installing symfony/http-client (v4.4.9): Downloading (100%)
  - Installing symfony/finder (v4.4.9): Downloading (100%)
  - Installing psr/http-factory (1.0.1): Downloading (100%)
  - Installing psr/http-client (1.0.1): Downloading (100%)
Writing lock file
Generating optimized autoload files
```

4. Generate the application key with `docker-compose exec web php artisan key:generate`.

```
$ docker-compose exec web php artisan key:generate
Application key [base64:TK5L6qgG1U9QxhZfhjPJHVqpVgHn3yQN8HxKDU/3zR4=] set successfully.
```

5. Run the migrations with `docker-compose exec web php artisan migrate`.

```
$ docker-compose exec web php artisan migrate
Migration table created successfully.
Migrated: 2014_10_12_000000_create_users_table
Migrated: 2014_10_12_100000_create_password_resets_table
Migrated: 2019_08_19_000000_create_failed_jobs_table
```

6. Access the application at `http://localhost`.

## Helpful links
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Laravel Documentation](https://laravel.com/docs)

onelinerhub: [How do I use Docker Compose to deploy a Laravel application in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-docker-compose-to-deploy-a-laravel-application-in-php)