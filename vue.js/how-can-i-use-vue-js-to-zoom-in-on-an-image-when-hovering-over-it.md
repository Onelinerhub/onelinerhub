# How can I use Vue.js to zoom in on an image when hovering over it?
// plain

Using Vue.js to zoom in on an image when hovering over it is a relatively simple task. The following example code will do the job:

```
<template>
  <div>
    <img
      :style="{ transform: `scale(${scale})` }"
      @mouseenter="scale = 2"
      @mouseleave="scale = 1"
      src="example.jpg"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      scale: 1,
    };
  },
};
</script>
```

When the mouse hovers over the image, the `scale` variable is set to `2`, which is then used in the `transform` style to zoom in on the image. When the mouse leaves the image, the `scale` variable is set back to `1`.

## Code explanation


- `template`: The HTML markup used to display the image.
- `@mouseenter`: A Vue.js directive that is triggered when the mouse enters the image.
- `@mouseleave`: A Vue.js directive that is triggered when the mouse leaves the image.
- `:style`: A Vue.js directive used to apply styles to the image.
- `transform`: A CSS style used to scale the image.
- `scale`: A data variable used to set the zoom level of the image.

## Helpful links

- [Vue.js Directives](https://vuejs.org/v2/api/#Directives)
- [CSS transform Property](https://www.w3schools.com/cssref/css3_pr_transform.asp)

onelinerhub: [How can I use Vue.js to zoom in on an image when hovering over it?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-zoom-in-on-an-image-when-hovering-over-it)