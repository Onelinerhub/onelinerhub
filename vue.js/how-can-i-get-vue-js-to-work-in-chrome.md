# How can I get Vue.js to work in Chrome?
// plain

To get Vue.js to work in Chrome, you need to do the following:

1. Include the Vue.js library in your HTML page.
```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

2. Create a new Vue instance, and define the data and methods you want to use.
```
<script>
  new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    },
    methods: {
      sayHello: function() {
        alert(this.message);
      }
    }
  });
</script>
```

3. Create an HTML element to hold the Vue instance.
```
<div id="app">
  {{ message }}
  <button @click="sayHello">Say Hello</button>
</div>
```

4. Open the HTML page in the Chrome browser.

5. You should see the output of the Vue instance in the browser window.

## Helpful links
- [Vue.js Documentation](https://vuejs.org/v2/guide/)
- [CDN for Vue.js](https://cdn.jsdelivr.net/npm/vue/dist/vue.js)

onelinerhub: [How can I get Vue.js to work in Chrome?](https://onelinerhub.com/vue.js/how-can-i-get-vue-js-to-work-in-chrome)