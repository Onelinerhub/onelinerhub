# How can I use a Vue.js UI kit to create a user interface?
// plain

Using a Vue.js UI kit to create a user interface is a great way to quickly get up and running with a modern web UI. The following example shows how to use a Vue.js UI kit to create a simple navigation bar with a search bar:

```
<template>
  <div>
    <vk-nav>
      <vk-nav-item href="#" title="Home" />
      <vk-nav-item href="#" title="About" />
    </vk-nav>
    <vk-search-bar placeholder="Search..." />
  </div>
</template>

<script>
import { VkNav, VkNavItem, VkSearchBar } from 'vue-kit';

export default {
  components: {
    VkNav,
    VkNavItem,
    VkSearchBar
  }
};
</script>
```

This code would produce a navigation bar with two items ("Home" and "About") and a search bar.

## Code explanation


* `<template>`: This is where the HTML markup is written.
* `<vk-nav>`: This is the Vue.js UI kit component for the navigation bar.
* `<vk-nav-item>`: This is the Vue.js UI kit component for the navigation items.
* `<vk-search-bar>`: This is the Vue.js UI kit component for the search bar.
* `import`: This is used to import the necessary components from the Vue.js UI kit.
* `components`: This is where the imported components are registered.

For more information on using Vue.js UI kits, see the [Vue.js documentation](https://vuejs.org/v2/guide/installation.html).

onelinerhub: [How can I use a Vue.js UI kit to create a user interface?](https://onelinerhub.com/vue.js/how-can-i-use-a-vue-js-ui-kit-to-create-a-user-interface)