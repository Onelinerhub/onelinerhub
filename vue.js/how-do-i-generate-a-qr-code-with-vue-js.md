# How do I generate a QR code with Vue.js?
// plain

Generating a QR code with Vue.js is relatively simple. To do so, you will need to use a library such as [vue-qrcode-reader](https://www.npmjs.com/package/vue-qrcode-reader).

First, install the library with the command `npm install vue-qrcode-reader` or `yarn add vue-qrcode-reader` depending on your package manager.

Then, import the library in your Vue component as follows:

```javascript
import QrReader from 'vue-qrcode-reader'

export default {
  components: {
    QrReader
  }
}
```

Finally, use the `qr-code` component in your template to render the QR code.

```html
<template>
  <qr-code @decode="onDecode" />
</template>
```

The `@decode` event will be triggered when the QR code is successfully decoded.

For more information, please refer to the [documentation](https://www.npmjs.com/package/vue-qrcode-reader#readme).

onelinerhub: [How do I generate a QR code with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-generate-a-qr-code-with-vue-js)