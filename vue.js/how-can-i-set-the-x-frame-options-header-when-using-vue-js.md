# How can I set the x-frame-options header when using Vue.js?
// plain

The X-Frame-Options header is an HTTP response header that can be used to indicate whether a browser should be allowed to render a page in a <frame>, <iframe>, <embed>, or <object> HTML element.

To set the X-Frame-Options header when using Vue.js, you can use the [vue-meta](https://github.com/nuxt/vue-meta) package.

Here is an example of setting the X-Frame-Options header using vue-meta:

```
import Vue from 'vue'
import Meta from 'vue-meta'

Vue.use(Meta)

export default {
  metaInfo: {
    meta: [
      {
        name: 'X-Frame-Options',
        content: 'DENY'
      }
    ]
  }
}
```

This example sets the X-Frame-Options header to `DENY`, which prevents the page from being rendered in any frames.

The `vue-meta` package provides a number of other options for setting the X-Frame-Options header, such as `SAMEORIGIN` and `ALLOW-FROM`. For more information, see the [vue-meta documentation](https://github.com/nuxt/vue-meta#x-frame-options).

onelinerhub: [How can I set the x-frame-options header when using Vue.js?](https://onelinerhub.com/vue.js/how-can-i-set-the-x-frame-options-header-when-using-vue-js)