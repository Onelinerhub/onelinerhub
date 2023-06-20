# player

How can I create an audio player using Vue.js?
// plain

Using Vue.js, you can create an audio player with the following steps:

1. Set up the HTML structure. Create a `<div>` element with an `id` attribute for the audio player.
```
<div id="audio-player"></div>
```

2. Add the Vue instance. Create a Vue instance with the `el` property set to the `id` of the `<div>` element.
```
const app = new Vue({
  el: '#audio-player',
});
```

3. Add the audio source. Create an `audio` element within the `<div>` and set the `src` attribute to the audio file you want to play.
```
<div id="audio-player">
  <audio src="audio.mp3"></audio>
</div>
```

4. Add the controls. Add `<button>` elements for the audio controls such as play, pause, and stop.
```
<div id="audio-player">
  <audio src="audio.mp3"></audio>
  <button>Play</button>
  <button>Pause</button>
  <button>Stop</button>
</div>
```

5. Add the logic. Add the logic to the `Vue` instance to control the audio player. This can be done using `methods` and `data` properties.
```
const app = new Vue({
  el: '#audio-player',
  data: {
    audio: null,
  },
  methods: {
    play() {
      this.audio.play();
    },
    pause() {
      this.audio.pause();
    },
    stop() {
      this.audio.pause();
      this.audio.currentTime = 0;
    },
  },
});
```

6. Add event listeners. Add event listeners to the `<audio>` element to handle the playback of the audio.
```
const app = new Vue({
  el: '#audio-player',
  data: {
    audio: null,
  },
  methods: {
    play() {
      this.audio.play();
    },
    pause() {
      this.audio.pause();
    },
    stop() {
      this.audio.pause();
      this.audio.currentTime = 0;
    },
  },
  mounted() {
    this.audio = document.querySelector('audio');
    this.audio.addEventListener('ended', this.stop);
  },
});
```

7. Add the styling. Add the styling to the audio player using CSS.

## Helpful links
- [Vue Documentation](https://vuejs.org/v2/guide/)
- [MDN Audio Element Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)

onelinerhub: [player

How can I create an audio player using Vue.js?](https://onelinerhub.com/vue.js/player--how-can-i-create-an-audio-player-using-vue-js)