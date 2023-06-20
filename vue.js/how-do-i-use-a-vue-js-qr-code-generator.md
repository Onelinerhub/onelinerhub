# How do I use a Vue.js QR code generator?
// plain

Using a Vue.js QR code generator is a very simple process. To begin, you will need to install the `vue-qrcode-reader` package. This can be done using the following command:

```
npm install vue-qrcode-reader
```

Once the package is installed, you can import the package into your Vue component.

```
import QRCodeReader from 'vue-qrcode-reader'
```

Next, you will need to register the component globally so it can be used throughout your application.

```
Vue.component('qr-code-reader', QRCodeReader)
```

Then, you can use the `qr-code-reader` component in your template.

```
<qr-code-reader @decode="onDecode" />
```

Finally, you will need to define the `onDecode` function which will be executed when a QR code is decoded. This function should accept the decoded data as an argument.

```
methods: {
  onDecode(data) {
    // Do something with the decoded data
  }
}
```

## Helpful links

* [vue-qrcode-reader on npm](https://www.npmjs.com/package/vue-qrcode-reader)
* [vue-qrcode-reader on GitHub](https://github.com/xkeshi/vue-qrcode-reader)

onelinerhub: [How do I use a Vue.js QR code generator?](https://onelinerhub.com/vue.js/how-do-i-use-a-vue-js-qr-code-generator)