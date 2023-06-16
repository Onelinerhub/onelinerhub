# How can I use Laravel Dusk to test my PHP application?
// plain

Laravel Dusk is a powerful browser automation tool that can be used to test a PHP application. It allows you to write tests that interact with your application like a real user.

To use Laravel Dusk, you need to install the Dusk package via Composer.

```
composer require --dev laravel/dusk
```

Once the package is installed, you need to create a `DuskTestCase` class. This class will be used to define and run your Dusk tests.

```
<?php

namespace Tests;

use Laravel\Dusk\TestCase as BaseTestCase;
use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\Remote\DesiredCapabilities;

abstract class DuskTestCase extends BaseTestCase
{
    use CreatesApplication;

    /**
     * Prepare for Dusk test execution.
     *
     * @beforeClass
     * @return void
     */
    public static function prepare()
    {
        static::startChromeDriver();
    }

    /**
     * Create the RemoteWebDriver instance.
     *
     * @return \Facebook\WebDriver\Remote\RemoteWebDriver
     */
    protected function driver()
    {
        $options = (new ChromeOptions)->addArguments([
            '--disable-gpu',
            '--headless',
            '--window-size=1920,1080',
        ]);

        return RemoteWebDriver::create(
            'http://localhost:9515', DesiredCapabilities::chrome()->setCapability(
                ChromeOptions::CAPABILITY, $options
            )
        );
    }
}
```

Once the `DuskTestCase` is created, you can create test classes that extend it. Each test class will contain the tests you want to run.

```
<?php

namespace Tests;

use Tests\DuskTestCase;
use Laravel\Dusk\Browser;

class ExampleTest extends DuskTestCase
{
    /**
     * A basic browser test example.
     *
     * @return void
     */
    public function testBasicExample()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/')
                    ->assertSee('Laravel');
        });
    }
}
```

Once the tests are written, you can run them using the Dusk command:

```
php artisan dusk
```

This will run your tests and provide a report of the results.

## Helpful links

- [Laravel Dusk Documentation](https://laravel.com/docs/master/dusk)
- [Laravel Dusk GitHub Repository](https://github.com/laravel/dusk)

onelinerhub: [How can I use Laravel Dusk to test my PHP application?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-dusk-to-test-my-php-application)