# How can I use Vue.js to implement internationalization (i18n)?
// plain

Vue.js provides an official plugin for internationalization (i18n) called [vue-i18n](https://kazupon.github.io/vue-i18n/). It provides an easy way to add internationalization support to Vue.js applications. Here is an example of how to use vue-i18n in a Vue.js application:

```javascript
import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: 'en',
  messages: {
    en: {
      hello: 'Hello World!'
    },
    fr: {
      hello: 'Bonjour le monde!'
    }
  }
})

new Vue({
  i18n,
  render: h => h(App)
}).$mount('#app')
```

In the code above:

1. The `VueI18n` plugin is imported and `Vue.use()` is called to install the plugin.
2. The `VueI18n` instance is created with the `locale` option set to `en` and a `messages` object containing translations for `en` and `fr`.
3. The `VueI18n` instance is passed to the `Vue` instance when it is created.

You can then use the `$t` method in the component to get the translated string:

```javascript
<template>
  <div>{{ $t('hello') }}</div>
</template>
```

This will output `Hello World!` if the `locale` is set to `en` and `Bonjour le monde!` if the `locale` is set to `fr`.

For more information, please see the [vue-i18n documentation](https://kazupon.github.io/vue-i18n/).

onelinerhub: [How can I use Vue.js to implement internationalization (i18n)?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-implement-internationalization--i--n-)