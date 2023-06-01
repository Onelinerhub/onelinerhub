# How can I use the AWS PHP SDK to manage Route53 records?
// plain

The AWS PHP SDK can be used to manage Route53 records. The following example code will list all the hosted zones in your account:

```php
<?php
require 'vendor/autoload.php';

use Aws\Route53\Route53Client;

$client = new Route53Client([
    'profile' => 'default',
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

$result = $client->listHostedZones();

foreach ($result['HostedZones'] as $zone) {
    echo $zone['Name'] . "\n";
}
```
## Output example

```
example.com.
```

## Code explanation


1. Require the autoloader, so that we can use the SDK: `require 'vendor/autoload.php';`
2. Use the `Aws\Route53\Route53Client` class to create a new client: `$client = new Route53Client([ ... ]);`
3. Call the `listHostedZones` method on the client to list all the hosted zones in the account: `$result = $client->listHostedZones();`
4. Iterate over the `HostedZones` array in the result and echo the `Name` of each: `echo $zone['Name'] . "\n";`

For more information, see the [AWS PHP SDK documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html) and the [Route53 API reference](https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html).

onelinerhub: [How can I use the AWS PHP SDK to manage Route53 records?](https://onelinerhub.com/php-aws/how-can-i-use-the-aws-php-sdk-to-manage-route---records)