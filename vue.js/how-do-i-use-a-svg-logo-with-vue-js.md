# How do I use a SVG logo with Vue.js?
// plain

To use a SVG logo with Vue.js, you can use the `<img>` tag and set the `src` attribute to the SVG file. For example:

```
<img src="logo.svg" alt="Logo">
```

This will render the logo as an image.

If you want to use the SVG code directly in the HTML, you can use the `<svg>` tag. For example:

```
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
  <circle cx="100" cy="100" r="100" fill="red"/>
</svg>
```

This will render a red circle.

You can also use the `vue-svg-loader` package to include SVG files in your Vue components. For example:

```
<template>
  <svg-icon icon="logo" />
</template>

<script>
  import SvgIcon from 'vue-svg-loader/SvgIcon.vue'

  export default {
    components: {
      SvgIcon
    }
  }
</script>
```

This will render the logo as an SVG icon.

## Code explanation

- `<img>` tag with `src` attribute to the SVG file
- `<svg>` tag with SVG code
- `vue-svg-loader` package with `SvgIcon` component

## Helpful links
- [Using SVG with Vue](https://vuejs.org/v2/guide/components-svg.html)
- [vue-svg-loader](https://github.com/visualfanatic/vue-svg-loader)

onelinerhub: [How do I use a SVG logo with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-a-svg-logo-with-vue-js)