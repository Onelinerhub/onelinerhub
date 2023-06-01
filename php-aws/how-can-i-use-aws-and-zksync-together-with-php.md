# How can I use AWS and Zksync together with PHP?
// plain

You can use AWS and Zksync together with PHP through the Zksync PHP SDK. This SDK provides a set of functions to interact with the Zksync blockchain.

To use the SDK, first install it using composer:
```
composer require zksync/zksync-php
```

Then, you can use the SDK to interact with the Zksync blockchain. For example, to create an account on the blockchain, you can use the following code:

```php
<?php
require 'vendor/autoload.php';

use ZkSync\Toolkit\Zksync;

$zksync = new Zksync('http://localhost:3030');
$account = $zksync->createAccount();

print_r($account);
```

The output of this code will be an array containing the account address and the private key:
```
Array
(
    [address] => 0x...
    [private_key] => 0x...
)
```

The SDK also provides functions to execute transactions, query the blockchain, and more. For more information, please refer to the [Zksync PHP SDK documentation](https://zksync.github.io/php-zksync-sdk/).

You can also use AWS to deploy the Zksync node and run the SDK on the same machine. For more information, please refer to the [AWS documentation](https://aws.amazon.com/documentation/).

onelinerhub: [How can I use AWS and Zksync together with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-aws-and-zksync-together-with-php)