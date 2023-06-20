# How can I use Vue.js with an ESP32 microcontroller?
// plain

You can use Vue.js with an ESP32 microcontroller by using the [Vue.js ESP32 port](https://github.com/vuejs-esp32/vuejs-esp32). This port allows you to write code for the ESP32 in Vue.js and compile it for the ESP32.

For example, the following code will create a simple ESP32 program that prints "Hello World!" to the serial port:

```javascript
import { Serial } from 'vuejs-esp32'

let serial = new Serial(115200)

serial.println('Hello World!')
```

This code will print the following output to the serial port:

```
Hello World!
```

The code consists of the following parts:

1. The `import` statement imports the `Serial` class from the `vuejs-esp32` package.
2. The `let serial` statement creates a new instance of the `Serial` class with a baud rate of 115200.
3. The `serial.println('Hello World!')` statement prints the string `Hello World!` to the serial port.

For more information about using Vue.js with the ESP32, please refer to the [Vue.js ESP32 Documentation](https://vuejs-esp32.github.io/docs/).

onelinerhub: [How can I use Vue.js with an ESP32 microcontroller?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-with-an-esp---microcontroller)