# How do I set a z-index in Vue.js?
// plain

To set a z-index in Vue.js, you can use the `z-index` property of the `style` attribute. The `z-index` property determines the order of overlapping elements. For example, the element with a higher `z-index` will appear on top of the element with a lower `z-index`.

## Example code

```
<div id="element1" style="position: absolute; z-index: 10;">
  Element 1
</div>
<div id="element2" style="position: absolute; z-index: 5;">
  Element 2
</div>
```

In the example code above, `element1` will appear above `element2` because it has a higher `z-index`.

The `style` attribute can be set directly in the HTML, or it can be set using a Vue directive. In the following example, the `style` attribute is set using the `v-bind` directive:

## Example code

```
<div id="element1" v-bind:style="{ position: 'absolute', zIndex: 10 }">
  Element 1
</div>
<div id="element2" v-bind:style="{ position: 'absolute', zIndex: 5 }">
  Element 2
</div>
```

In this example, `element1` will again appear above `element2` because it has a higher `z-index`.

The parts of the code are as follows:

- `z-index` - The property used to set the order of overlapping elements
- `style` - The attribute used to set the `z-index` property
- `v-bind` - The Vue directive used to set the `style` attribute

For more information, see the [Vue.js documentation](https://vuejs.org/v2/guide/class-and-style.html#Binding-Inline-Styles).

onelinerhub: [How do I set a z-index in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-set-a-z-index-in-vue-js)