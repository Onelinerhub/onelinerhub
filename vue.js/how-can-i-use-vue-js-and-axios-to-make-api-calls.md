# How can I use Vue.js and Axios to make API calls?
// plain

You can use Vue.js and Axios to make API calls with the following steps:

1. Install Axios:
   `npm install axios`

2. Create a Vue instance:
   ```
   const app = new Vue({
     el: '#app',
     data: {
        //data
     }
   })
   ```

3. Make the API call using Axios:
   ```
   axios.get('https://example.com/api/endpoint')
     .then(function (response) {
       // handle success
       console.log(response);
     })
     .catch(function (error) {
       // handle error
       console.log(error);
     })
   ```

4. Handle the response:
   ```
   app.data = response.data;
   ```

5. Render the response data in the view:
   ```
   <div v-for="item in data">
     {{ item.name }}
   </div>
   ```

You can find more information and examples of using Vue.js and Axios to make API calls in the [Vue.js documentation](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) and the [Axios documentation](https://github.com/axios/axios).

onelinerhub: [How can I use Vue.js and Axios to make API calls?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-and-axios-to-make-api-calls)