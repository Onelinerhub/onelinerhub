# How do I use Vue.js and Bootstrap to create a modal?
// plain

Using Vue.js and Bootstrap together is a great way to create a modal. To do so, you'll need to install both Bootstrap and Vue.js.

Once you have both installed, you will need to create the modal component. Here is an example of a modal component written in Vue.js:

```
<template>
  <div>
    <div class="modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>Modal body text goes here.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary">Save changes</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
```

The template above contains the necessary HTML elements for a Bootstrap modal. It includes a modal header, body, and footer. The modal header contains a title and close button, the modal body contains the text for the modal, and the modal footer contains two buttons.

To show the modal, you will need to add a few lines of Vue.js code to the component. Here is an example of how to show the modal when a button is clicked:

```
<template>
  <div>
    <button type="button" @click="showModal = true">Show Modal</button>
    <div class="modal" v-show="showModal" tabindex="-1" role="dialog">
      ...
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false
    }
  }
}
</script>
```

In the code above, the `showModal` variable is used to control whether the modal is visible or not. When the button is clicked, the `showModal` variable is set to `true`, which will cause the modal to be visible.

To hide the modal, you can add a close button to the modal footer and set the `showModal` variable to `false` when the button is clicked.

## Helpful links

- [Bootstrap](https://getbootstrap.com/)
- [Vue.js](https://vuejs.org/)

onelinerhub: [How do I use Vue.js and Bootstrap to create a modal?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-and-bootstrap-to-create-a-modal)