# How do I use websockets with Vue.js?
// plain

Websockets can be used with Vue.js to create real-time applications. To use websockets with Vue.js, the `vue-native-websocket` library can be used.

To install the library, run the following command:
```
npm install vue-native-websocket
```

Once installed, the library can be imported and used in the Vue component.
```
import VueNativeSock from 'vue-native-websocket'

export default {
  name: 'MyComponent',
  data () {
    return {
      message: ''
    }
  },
  sockets: {
    connect: function () {
      console.log('Socket connected')
    },
    customEmit: function (val) {
      this.message = val
    }
  },
  methods: {
    sendMessage: function () {
      this.$socket.emit('emit_method', 'Hello World')
    }
  }
}
```
In the above example, the `vue-native-websocket` library is imported and used in the component. The `sockets` object is used to define the websocket connection and the `connect` and `customEmit` methods. The `connect` method is called when the websocket connection is established and the `customEmit` method is called when a message is received from the server. The `sendMessage` method is used to emit a message to the server.

## Code explanation


1. `import VueNativeSock from 'vue-native-websocket'` - This line imports the `vue-native-websocket` library.
2. `sockets: {` - This object is used to define the websocket connection and the methods that will be called when the websocket connection is established and when a message is received from the server.
3. `connect: function () {` - This method is called when the websocket connection is established.
4. `customEmit: function (val) {` - This method is called when a message is received from the server.
5. `sendMessage: function () {` - This method is used to emit a message to the server.

## Helpful links

- [vue-native-websocket](https://www.npmjs.com/package/vue-native-websocket)

onelinerhub: [How do I use websockets with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-websockets-with-vue-js)