# How do I set environment variables in an Elastic Beanstalk PHP environment?
// plain

Setting environment variables in an Elastic Beanstalk PHP environment can be done in a few steps:

1. Create a `.ebextensions` directory in the root of your project
2. Create a file named `env.config` in the `.ebextensions` directory
3. Add the following code to the `env.config` file, replacing the `MY_VAR` and `my_value` with your own environment variable name and value:

```
option_settings:
  - namespace: aws:elasticbeanstalk:application:environment
    option_name: MY_VAR
    value: my_value
```

4. Deploy your project to Elastic Beanstalk
5. Your environment variable is now set

## Helpful links
- [Elastic Beanstalk Documentation - Configuration Files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)

onelinerhub: [How do I set environment variables in an Elastic Beanstalk PHP environment?](https://onelinerhub.com/php-elastica/how-do-i-set-environment-variables-in-an-elastic-beanstalk-php-environment)