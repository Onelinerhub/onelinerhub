# How can I use Vue.js to create a XSS payload?
// plain

XSS payloads can be created using Vue.js by binding user-controlled data to the DOM. This can be done using `v-html` directive, which binds user data to the DOM. The following example code block shows how to do this:

```
<div id="app">
  <div v-html="userInput"></div>
</div>

<script>
  new Vue({
    el: '#app',
    data: {
      userInput: '<script>alert("XSS")</script>'
    }
  })
</script>
```

This code will create an XSS payload and display an alert window with the text "XSS".

The code can be broken down into the following parts:

1. `<div id="app">`: A div element with the id of "app". This is used to identify the Vue instance.
2. `<div v-html="userInput"></div>`: A div element with the `v-html` directive. This binds the data from the `userInput` variable to the DOM.
3. `new Vue({`: This creates a new Vue instance.
4. `el: '#app',`: This is the element that the Vue instance will be attached to. In this case it is the div element with the id of "app".
5. `data: {`: This is the data that will be used in the Vue instance.
6. `userInput: '<script>alert("XSS")</script>'`: This is the user-controlled data that is bound to the DOM using the `v-html` directive.

For more information on creating XSS payloads with Vue.js, please see the following resources:

* [Vue.js Documentation](https://vuejs.org/v2/guide/syntax.html#Raw-HTML)
* [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

onelinerhub: [How can I use Vue.js to create a XSS payload?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-create-a-xss-payload)