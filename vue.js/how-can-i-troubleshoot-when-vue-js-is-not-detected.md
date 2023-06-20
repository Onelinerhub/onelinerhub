# How can I troubleshoot when Vue.js is not detected?
// plain

1. Check if Vue.js is included in the HTML page correctly. Make sure that the script tag is pointing to the correct version of Vue.js and that it is included before any other scripts. Eg:
```
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.js"></script>
```

2. Check the browser console for any errors. If there are any errors, it may be related to the script tag or the version of Vue.js being used.

3. Check if the Vue object is defined. To do this, open the browser console and type ```console.log(Vue)```. If Vue is detected, the object should be printed in the console.

4. Check if the Vue instance is created correctly. To do this, create a new Vue instance and check if it is created correctly. Eg:
```
const app = new Vue({
  el: '#app'
})
```
If the Vue instance is created correctly, the browser console should show a message like ```[Vue warn]: You are using the runtime-only build of Vue where the template compiler is not available. Either pre-compile the templates into render functions, or use the compiler-included build.```

5. Check the network tab in the browser console to make sure that the Vue.js script is actually being loaded.

6. If all the above steps fail, try reinstalling Vue.js using the command ```npm install vue```

7. If the issue persists, check out the [Vue.js troubleshooting guide](https://vuejs.org/v2/guide/troubleshooting.html) for more detailed information.

onelinerhub: [How can I troubleshoot when Vue.js is not detected?](https://onelinerhub.com/vue.js/how-can-i-troubleshoot-when-vue-js-is-not-detected)