# How can I embed a YouTube video in a Vue.js application?
// plain

In order to embed a YouTube video in a Vue.js application, we can use the `vue-youtube` package from npm. This package provides a Vue component that can be used to embed a YouTube video with various options.

Below is an example of how to use the `vue-youtube` package to embed a YouTube video:

```
<template>
  <div>
    <youtube
      :video-id="videoId"
      @ready="onReady"
      @state-change="onStateChange"
    />
  </div>
</template>

<script>
import Youtube from 'vue-youtube'

export default {
  components: {
    Youtube
  },
  data() {
    return {
      videoId: 'M7lc1UVf-VE'
    }
  },
  methods: {
    onReady(event) {
      // access to player in all event handlers via event.target
      event.target.playVideo()
    },
    onStateChange(event) {
      console.log('player state', event.data)
    }
  }
}
</script>
```

The example code above will embed a YouTube video with the ID `M7lc1UVf-VE`.

## Code explanation

* `<youtube>` - This is the component that is imported from the `vue-youtube` package.
* `:video-id="videoId"` - This is the prop that is used to specify the ID of the YouTube video.
* `@ready="onReady"` - This is the event handler that is triggered when the YouTube video is ready.
* `@state-change="onStateChange"` - This is the event handler that is triggered when the state of the YouTube video changes.
* `event.target.playVideo()` - This is the method that is used to play the YouTube video.

## Helpful links
* [vue-youtube package](https://www.npmjs.com/package/vue-youtube)
* [YouTube Player API Reference for iframe Embeds](https://developers.google.com/youtube/iframe_api_reference)

onelinerhub: [How can I embed a YouTube video in a Vue.js application?](https://onelinerhub.com/vue.js/how-can-i-embed-a-youtube-video-in-a-vue-js-application)