# How do I create a PHP AWS Lambda function?
// plain

Creating a PHP AWS Lambda function is a relatively straightforward process.

1. Create a new Lambda Function in the AWS Console.
2. Select the "Author from scratch" option and choose a Runtime of "PHP 7.3".
3. Create a new role or select an existing role with permissions to access other AWS services.
4. Enter a function name and description, and then click the "Create Function" button.
5. Create a new folder and copy the following code into a new file called "index.php".

```
<?php
  function handler($event, $context) {
      return ["message" => "Hello World!"];
  }
?>
```

6. Zip up the folder containing the file and upload it to the Lambda Function.
7. Test the function and you should see the output `{"message":"Hello World!"}`

This is just a basic example of how to create a PHP AWS Lambda function. For more information on creating and deploying Lambda functions, see the [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/index.html).

onelinerhub: [How do I create a PHP AWS Lambda function?](https://onelinerhub.com/php-aws/how-do-i-create-a-php-aws-lambda-function)