# How do I use the PHP AWS SDK to access documentation?
// plain

The PHP AWS SDK can be used to access documentation through the use of the **Aws\Docs** class. This class provides access to the AWS documentation page, allowing you to search for specific topics, and view the related documentation.

Here is an example of how to use the **Aws\Docs** class to access the AWS documentation page:

```php
use Aws\Docs;
$docs = new Docs();
$result = $docs->search('S3');
```

This will return an array of search results related to S3.

## Code explanation


1. `use Aws\Docs;` - This imports the **Aws\Docs** class into the code.
2. `$docs = new Docs();` - This creates a new instance of the **Aws\Docs** class.
3. `$result = $docs->search('S3');` - This calls the **Aws\Docs::search()** method, passing in the term 'S3' as the search parameter.

## Helpful links

- [AWS SDK for PHP Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Docs.Docs.html)
- [AWS Documentation](https://aws.amazon.com/documentation/)

onelinerhub: [How do I use the PHP AWS SDK to access documentation?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-sdk-to-access-documentation)