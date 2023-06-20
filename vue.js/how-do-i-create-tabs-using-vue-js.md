# How do I create tabs using Vue.js?
// plain

Using Vue.js, you can create tabs for your webpages by making use of the `<tabs>` and `<tab>` components.

## Example code

```
<tabs>
  <tab name="Home"> Home Content </tab>
  <tab name="About"> About Content </tab>
  <tab name="Contact"> Contact Content </tab>
</tabs>
```

This will create three tabs with the names "Home", "About" and "Contact". Clicking on each tab will show the content associated with it.

## Code explanation

- `<tabs>`: This is the parent component which will contain all of the tabs.
- `<tab>`: This is the component for each individual tab. It takes a `name` prop which will be the name of the tab.
- `name`: This is the name of the tab which will be displayed on the tab itself.
- `Home Content`, `About Content` and `Contact Content`: These are the contents that will be displayed when the corresponding tab is clicked.

## Helpful links
- [Vue.js Tabs Documentation](https://vuejs.org/v2/examples/tabs.html)
- [Vue.js Components Documentation](https://vuejs.org/v2/guide/components.html)

onelinerhub: [How do I create tabs using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-create-tabs-using-vue-js)