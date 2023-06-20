# How do I use an SVG icon in Vue.js?
// plain

Using an SVG icon in Vue.js is a great way to add visual flair to your application. Here is an example of how to do it:

```html
<template>
  <svg>
    <use xlink:href="@/assets/icons.svg#icon-name"></use>
  </svg>
</template>
```

The `<svg>` tag is used to create a container for the icon. The `<use>` tag is then used to reference the icon from the SVG sprite file, which is located at `@/assets/icons.svg`. The `#icon-name` part of the `xlink:href` attribute is used to specify which icon should be used.

**Parts of the code:**

1. `<svg>`: This tag creates a container for the SVG icon.
2. `<use>`: This tag is used to reference the icon from the SVG sprite file.
3. `xlink:href`: This attribute of the `<use>` tag is used to specify which icon should be used.
4. `@/assets/icons.svg`: This is the path to the SVG sprite file containing the icon.
5. `#icon-name`: This part of the `xlink:href` attribute is used to specify which icon should be used.

**## Helpful links**

- [Vue.js Documentation - SVG](https://vuejs.org/v2/guide/syntax.html#SVG)
- [MDN - SVG <use> Element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/use)

onelinerhub: [How do I use an SVG icon in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-an-svg-icon-in-vue-js)