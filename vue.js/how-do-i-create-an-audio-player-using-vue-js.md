# How do I create an audio player using Vue.js?
// plain

Creating an audio player using Vue.js is an easy process. The following example code block will create an audio player with basic controls to play, pause, and adjust the volume.

```
<template>
  <div>
    <audio ref="audio" :src="audioSrc" />
    <button @click="play">Play</button>
    <button @click="pause">Pause</button>
    <input type="range" v-model="volume" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      audioSrc: 'audio.mp3',
      volume: 0.5
    }
  },
  methods: {
    play() {
      this.$refs.audio.play();
    },
    pause() {
      this.$refs.audio.pause();
    }
  }
};
</script>
```

The code above creates an audio player with three controls: a play button, a pause button, and a volume slider. The `ref` attribute is used to create a reference to the `<audio>` element so that we can call its methods from the script. The `@click` attribute is used to attach click event handlers to the buttons, and the `v-model` attribute is used to bind the volume slider to the `volume` data property.

## Code explanation


1. `<template>` - This is the HTML template for the audio player.
2. `<audio ref="audio" :src="audioSrc" />` - This creates an `<audio>` element with a reference to it and binds the `src` attribute to the `audioSrc` data property.
3. `<button @click="play">Play</button>` - This creates a play button and attaches a click event handler to it that calls the `play()` method.
4. `<button @click="pause">Pause</button>` - This creates a pause button and attaches a click event handler to it that calls the `pause()` method.
5. `<input type="range" v-model="volume" />` - This creates a volume slider and binds it to the `volume` data property.
6. `data()` - This function returns the data properties for the audio player.
7. `methods` - This object contains the methods for the audio player.

For more information on creating audio players with Vue.js, see the [Vue.js documentation](https://vuejs.org/v2/guide/components.html#Using-v-model-on-Components).

onelinerhub: [How do I create an audio player using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-create-an-audio-player-using-vue-js)