# How do I change the z-index of a modal in Vue.js?
// plain

To change the z-index of a modal in Vue.js, you can use the `z-index` property in your CSS. This property sets the stack order of the modal, and is a number greater than or equal to 0.

For example, to set the z-index of a modal to 999, you can use the following code:

```
<style>
  .modal {
    z-index: 999;
  }
</style>
```

## Code explanation


1. `.modal`: The CSS selector that selects the modal element.
2. `z-index`: The CSS property that sets the stack order of the modal.
3. `999`: The value of the z-index property which sets the modal's stack order to 999.

## Helpful links

- [MDN Web Docs - z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index)
- [Vue.js Documentation - Styling](https://vuejs.org/v2/guide/class-and-style.html)

onelinerhub: [How do I change the z-index of a modal in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-change-the-z-index-of-a-modal-in-vue-js)