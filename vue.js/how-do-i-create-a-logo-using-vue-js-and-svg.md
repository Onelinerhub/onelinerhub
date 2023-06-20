# How do I create a logo using Vue.js and SVG?
// plain

Creating a logo using Vue.js and SVG is relatively straightforward. To get started, create a new Vue.js project and add an `<svg>` element to the template. Then, use the `<rect>` and `<text>` elements to create the shape and text of the logo. To style the logo, use the `fill` and `stroke` attributes to set the color.

## Example code

```
<svg width="200" height="200">
  <rect x="10" y="10" width="180" height="180" fill="red" stroke="black" />
  <text x="90" y="90" font-size="50" text-anchor="middle" fill="black">Vue Logo</text>
</svg>
```

This code will output a red rectangle with a black border and a black "Vue Logo" text in the middle.

## Code explanation


- `<svg>` element: This element defines the SVG document.
- `<rect>` element: This element defines a rectangle with the given `x`, `y`, `width`, and `height` attributes.
- `fill` attribute: This attribute sets the fill color of the shape.
- `stroke` attribute: This attribute sets the border color of the shape.
- `<text>` element: This element defines a text element with the given `x`, `y`, `font-size`, and `text-anchor` attributes.
- `text-anchor` attribute: This attribute sets the alignment of the text.

## Helpful links

- [Vue.js Documentation](https://vuejs.org/v2/guide/)
- [SVG Tutorial](https://www.w3schools.com/graphics/svg_intro.asp)

onelinerhub: [How do I create a logo using Vue.js and SVG?](https://onelinerhub.com/vue.js/how-do-i-create-a-logo-using-vue-js-and-svg)