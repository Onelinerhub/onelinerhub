# How can I create a transition effect in Vue.js?
// plain

Vue.js provides a powerful transition system to easily apply transition effects to elements when they are inserted, updated or removed from the DOM. To create a transition effect, you need to add the `<transition>` element to your template. Within the `<transition>` element, you can specify the name of the transition effect, the duration of the transition, and the type of animation.

You can also define custom transition classes to apply to the element during the transition. For example, the following code creates a transition effect for a `<div>` element that will fade in and out over 500ms:

```html
<transition name="fade" duration="500">
  <div>My transition element</div>
</transition>
```

You can also add custom CSS classes to the transition element to control the transition effect. For example, the following code will apply the `fade-in` and `fade-out` classes to the `<div>` element during the transition:

```html
<transition name="fade" enter-class="fade-in" leave-class="fade-out" duration="500">
  <div>My transition element</div>
</transition>
```

To control the transition effect, you can also use the `<transition>` element's `before-enter` and `after-leave` hooks. These hooks allow you to define custom JavaScript functions to execute before or after the transition effect has been applied. For example, the following code will log a message to the console before and after the transition effect is applied:

```html
<transition name="fade" duration="500"
  before-enter="beforeEnter"
  after-leave="afterLeave"
>
  <div>My transition element</div>
</transition>
```

```js
// JavaScript
function beforeEnter(el) {
  console.log('Before enter');
}

function afterLeave(el) {
  console.log('After leave');
}
```

## Output example

```
Before enter
After leave
```

For more information, see the [Vue.js Transition & Animation documentation](https://vuejs.org/v2/guide/transitions.html).

onelinerhub: [How can I create a transition effect in Vue.js?](https://onelinerhub.com/vue.js/how-can-i-create-a-transition-effect-in-vue-js)