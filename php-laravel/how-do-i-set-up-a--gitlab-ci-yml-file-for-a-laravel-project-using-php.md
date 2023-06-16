# How do I set up a .gitlab-ci.yml file for a Laravel project using PHP?
// plain

The .gitlab-ci.yml file defines the CI/CD pipeline for your Laravel project. It is a YAML file that contains a set of instructions for the CI/CD system to follow.

Below is an example of a .gitlab-ci.yml file for a Laravel project using PHP:

```
image: php:7.4

stages:
  - build
  - test
  - deploy

cache:
  paths:
    - vendor/

before_script:
  - apt-get update -y
  - apt-get install -y unzip
  - curl -sS https://getcomposer.org/installer | php
  - php composer.phar install

build:
  stage: build
  script:
    - php artisan clear-compiled
    - php artisan optimize

test:
  stage: test
  script:
    - phpunit

deploy:
  stage: deploy
  script:
    - rsync -avz --delete ./ /var/www/
```

This .gitlab-ci.yml file defines three stages of the CI/CD pipeline: build, test, and deploy. The `image` section specifies the Docker image to use for the CI/CD pipeline. The `cache` section specifies the paths to cache, which will speed up subsequent builds. The `before_script` section contains commands that will be executed before any other commands. The `build` section contains commands for building the Laravel project. The `test` section contains commands for running the tests. The `deploy` section contains commands for deploying the project.

## Code explanation


- `image`: Specifies the Docker image to use for the CI/CD pipeline.
- `stages`: Specifies the stages of the CI/CD pipeline.
- `cache`: Specifies the paths to cache, which will speed up subsequent builds.
- `before_script`: Contains commands that will be executed before any other commands.
- `build`: Contains commands for building the Laravel project.
- `test`: Contains commands for running the tests.
- `deploy`: Contains commands for deploying the project.

## Helpful links

- [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [GitLab CI/CD for Laravel Projects](https://docs.gitlab.com/ee/ci/examples/laravel_with_gitlab_ci_cd/)

onelinerhub: [How do I set up a .gitlab-ci.yml file for a Laravel project using PHP?](https://onelinerhub.com/php-laravel/how-do-i-set-up-a--gitlab-ci-yml-file-for-a-laravel-project-using-php)