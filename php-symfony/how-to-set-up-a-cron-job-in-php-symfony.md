# How to set up a cron job in PHP Symfony?
// plain

Setting up a cron job in PHP Symfony is easy.

First, create a command class in the `src/Command` directory.

```php
<?php

namespace App\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

class MyCronJobCommand extends Command
{
    protected static $defaultName = 'app:my-cron-job';

    protected function configure()
    {
        $this
            ->setDescription('My cron job description.')
            ->setHelp('This command allows you to create a cron job...');
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        // Do something...
    }
}
```

Then, add the command to the `config/services.yaml` file:

```yaml
services:
    App\Command\MyCronJobCommand:
        tags:
            - { name: console.command }
```

Finally, add the cron job to the crontab file:

```
* * * * * cd /path-to-your-project && php bin/console app:my-cron-job
```

This will execute the command every minute.

## Helpful links

- [Symfony Console Component](https://symfony.com/doc/current/components/console.html)
- [Crontab Guru](https://crontab.guru/)

onelinerhub: [How to set up a cron job in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-set-up-a-cron-job-in-php-symfony)