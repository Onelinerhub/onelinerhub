# How do I use a QR code scanner in Vue.js?
// plain

Using a QR code scanner in Vue.js is relatively easy. To get started, you'll need to install the [vue-qrcode-reader](https://www.npmjs.com/package/vue-qrcode-reader) package. After that, you'll need to add a few lines of code to your Vue instance.

First, you'll need to import the package.

```
import VueQrcodeReader from 'vue-qrcode-reader'
Vue.use(VueQrcodeReader)
```

Next, you'll need to add the `<qrcode-reader>` component to your template.

```
<qrcode-reader @decode="onDecode" />
```

Finally, you'll need to define the `onDecode` function in your `methods` object. This function will be called when a QR code is successfully scanned.

```
methods: {
  onDecode (result) {
    console.log(result)
  }
}
```

The `result` argument of the `onDecode` function will contain the decoded data from the QR code.

For more information, see the [vue-qrcode-reader documentation](https://www.npmjs.com/package/vue-qrcode-reader).

onelinerhub: [How do I use a QR code scanner in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-a-qr-code-scanner-in-vue-js)