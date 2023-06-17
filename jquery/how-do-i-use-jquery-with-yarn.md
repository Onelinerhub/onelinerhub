# How do I use jQuery with Yarn?
// plain

Yarn is a package manager that allows you to install and manage packages for web development. jQuery is a popular JavaScript library used for DOM manipulation and AJAX requests. You can easily use jQuery with Yarn by installing the jQuery package.

To install jQuery with Yarn, run the following command in your terminal:

```
yarn add jquery
```

Yarn will then install the jQuery package and any of its dependencies.

Once installed, you can use jQuery in your code like this:

```
import $ from 'jquery';

$(document).ready(function() {
  console.log('jQuery is ready!');
});
```

The code above will log "jQuery is ready!" to the console when the document is ready.

You can also use Yarn to update jQuery to the latest version. To do this, run the following command in your terminal:

```
yarn upgrade jquery
```

Yarn will then update the jQuery package to the latest version.

For more information about using Yarn and jQuery together, see the [Yarn documentation](https://classic.yarnpkg.com/en/docs/usage/) and the [jQuery documentation](https://api.jquery.com/).

onelinerhub: [How do I use jQuery with Yarn?](https://onelinerhub.com/jquery/how-do-i-use-jquery-with-yarn)