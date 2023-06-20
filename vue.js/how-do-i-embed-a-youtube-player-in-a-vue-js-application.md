# How do I embed a YouTube player in a Vue.js application?
// plain

To embed a YouTube player in a Vue.js application, you can use the `vue-youtube` package. This package provides a Vue.js component that wraps the YouTube IFrame API.

To install the package, run the following command:
```
npm install vue-youtube
```

To use the `vue-youtube` component, you need to import it into your Vue.js application:
```javascript
import VueYoutube from 'vue-youtube'

Vue.use(VueYoutube)
```

Then, you can use the `<youtube>` component to embed the YouTube player in your application:
```html
<youtube video-id="lG0Ys-2d4MA"></youtube>
```

The `video-id` prop is used to specify the YouTube video that should be embedded.

## Helpful links
- [Vue.js](https://vuejs.org/)
- [vue-youtube](https://www.npmjs.com/package/vue-youtube)

onelinerhub: [How do I embed a YouTube player in a Vue.js application?](https://onelinerhub.com/vue.js/how-do-i-embed-a-youtube-player-in-a-vue-js-application)