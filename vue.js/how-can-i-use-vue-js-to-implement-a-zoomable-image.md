# How can I use Vue.js to implement a zoomable image?
// plain

Vue.js can be used to implement a zoomable image by utilizing the `v-zoom` directive. This directive allows you to bind a zoom value to an element, and it will automatically scale the element according to the zoom value.

For example, the following code will create an image that can be zoomed in and out using the mouse wheel:

```html
<div>
  <img v-zoom="zoom" src="my-image.jpg" />
</div>
```
```js
new Vue({
  el: '#app',
  data: {
    zoom: 1
  }
})
```

The `v-zoom` directive binds the `zoom` value in the Vue instance to the image element. When the `zoom` value changes, the image will be scaled accordingly.

The following code will bind the `zoom` value to the mouse wheel event, so that the image can be zoomed in and out using the mouse wheel:

```js
new Vue({
  el: '#app',
  data: {
    zoom: 1
  },
  methods: {
    handleWheel: function(e) {
      this.zoom += e.deltaY * -0.01
    }
  }
})
```
```html
<div @wheel="handleWheel">
  <img v-zoom="zoom" src="my-image.jpg" />
</div>
```

The `v-zoom` directive can be used with other elements, such as `div`s or `span`s, to create zoomable elements that are not images.

## Helpful links
- [Vue.js v-zoom Directive](https://vuejs.org/v2/api/#v-zoom)
- [Mouse Wheel Event](https://developer.mozilla.org/en-US/docs/Web/Events/wheel)

onelinerhub: [How can I use Vue.js to implement a zoomable image?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-implement-a-zoomable-image)