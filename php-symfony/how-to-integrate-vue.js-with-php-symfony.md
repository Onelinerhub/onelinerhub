# How to integrate Vue.js with PHP Symfony?
// plain

Integrating Vue.js with PHP Symfony is a straightforward process.

First, install the Symfony Encore package:
```
composer require symfony/webpack-encore-bundle
```

Then, create a webpack.config.js file in the root of your project:
```
// webpack.config.js

var Encore = require('@symfony/webpack-encore');

Encore
    // the project directory where all compiled assets will be stored
    .setOutputPath('public/build/')

    // the public path used by the web server to access the previous directory
    .setPublicPath('/build')

    // will create public/build/app.js and public/build/app.css
    .addEntry('app', './assets/js/app.js')

    // allow sass/scss files to be processed
    .enableSassLoader()

    // allow legacy applications to use $/jQuery as a global variable
    .autoProvidejQuery()

    .enableVueLoader()
;

// export the final configuration
module.exports = Encore.getWebpackConfig();
```

Finally, run the Encore command to compile the assets:
```
./node_modules/.bin/encore dev
```

The compiled assets can then be included in your Symfony templates:
```
<script src="{{ asset('build/app.js') }}"></script>
```

This will integrate Vue.js with your Symfony application.

## Helpful links
- [Symfony Encore Documentation](https://symfony.com/doc/current/frontend.html)
- [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [How to integrate Vue.js with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-integrate-vue.js-with-php-symfony)