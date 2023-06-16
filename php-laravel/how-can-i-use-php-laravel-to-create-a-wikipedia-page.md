# How can I use PHP Laravel to create a Wikipedia page?
// plain

Creating a Wikipedia page with PHP Laravel requires the use of the MediaWiki API. This API allows developers to access the functionality of the MediaWiki platform, including creating and editing pages.

To get started, you'll need to install the MediaWiki API package for Laravel. This can be done using Composer by running the following command:

```
composer require mediawiki/api
```

Once installed, you can begin making calls to the MediaWiki API. To create a new page, you can use the `edit` action. This action requires the page title, content, and edit summary as parameters. For example, to create a page titled "My Page" with the content "This is my page" and the edit summary "Creating page":

```php
<?php

use Mediawiki\Api\MediawikiApi;

$api = new MediawikiApi('https://en.wikipedia.org/w/api.php');

$api->edit('My Page', 'This is my page', 'Creating page');
```

The above code will create a page titled "My Page" with the given content and edit summary.

Here are some ## Helpful links

- [MediaWiki API Documentation](https://www.mediawiki.org/wiki/API:Main_page)
- [MediaWiki API Package for Laravel](https://github.com/mediawiki-utilities/mediawiki-api-laravel)

onelinerhub: [How can I use PHP Laravel to create a Wikipedia page?](https://onelinerhub.com/php-laravel/how-can-i-use-php-laravel-to-create-a-wikipedia-page)