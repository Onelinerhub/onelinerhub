# How can I use jQuery in a Vue.js project?
// plain

jQuery can be used in a Vue.js project by installing it via npm and then importing it into your main.js file. For example, you can install jQuery with the command:

```
npm install jquery
```

Once installed, you can import it into your main.js file like this:

```
import $ from 'jquery'
```

You can then use jQuery in your project by referencing it with the `$` symbol. For example, you could use the `.ready()` function to execute a callback after the DOM is loaded:

```
$(document).ready(function() {
  console.log('DOM is ready!');
});
```

## Output example

```
DOM is ready!
```

## Code explanation


1. `npm install jquery` - Installs jQuery via npm
2. `import $ from 'jquery'` - Imports jQuery into your main.js file
3. `$(document).ready(function() {...` - Uses the `.ready()` function to execute a callback after the DOM is loaded

## Helpful links

- [jQuery CDN](https://code.jquery.com/)
- [Using jQuery with Vue.js](https://vuejsdevelopers.com/2018/03/20/vue-js-jquery/)

onelinerhub: [How can I use jQuery in a Vue.js project?](https://onelinerhub.com/vue.js/how-can-i-use-jquery-in-a-vue-js-project)