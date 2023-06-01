# How do I set up an AWS PHP cron job?
// plain

Setting up an AWS PHP cron job requires a few steps.

1. Create a PHP script that will perform the task you want the cron job to do.
2. Set up an Amazon EC2 instance.
3. Connect to the instance using an SSH client.
4. Upload the PHP script to the instance.
5. Create a cron job using the `crontab -e` command.

For example, the following command will run the `my-script.php` file every minute:
```
* * * * * /usr/bin/php /path/to/my-script.php
```

6. Save the cron job and exit the editor.
7. Check the cron job log to make sure it is running correctly.

## Helpful links
* [AWS Documentation - Setting Up Cron Jobs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cron-jobs.html)
* [Digital Ocean - How To Use Cron To Automate Tasks On Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-on-ubuntu-1804)

onelinerhub: [How do I set up an AWS PHP cron job?](https://onelinerhub.com/php-aws/how-do-i-set-up-an-aws-php-cron-job)