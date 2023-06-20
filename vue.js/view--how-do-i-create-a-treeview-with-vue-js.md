# view

How do I create a treeview with Vue.js?
// plain

To create a treeview with Vue.js, you need to use the [Vue.js Tree View](https://github.com/vuejs-treeview/vue-treeview) library.

First, install the library using npm:
```
npm install vue-treeview
```

Then, import the library into your Vue component:
```
import VueTreeView from 'vue-treeview'
```

Next, register the VueTreeView component:
```
components: {
  VueTreeView
}
```

After that, define your data in the component:
```
data () {
  return {
    treeData: [
      {
        text: 'Fruits',
        nodes: [
          {
            text: 'Apple'
          },
          {
            text: 'Orange'
          }
        ]
      },
      {
        text: 'Vegetables',
        nodes: [
          {
            text: 'Carrot'
          },
          {
            text: 'Potato'
          }
        ]
      }
    ]
  }
}
```

Finally, render the treeview in the template:
```
<vue-treeview :data="treeData" />
```

This will render the following treeview:

![Vue.js Treeview](https://raw.githubusercontent.com/vuejs-treeview/vue-treeview/master/example/public/treeview.png)

## Helpful links
- [Vue.js Tree View Documentation](https://github.com/vuejs-treeview/vue-treeview)
- [Vue.js Tree View Demo](https://vuejs-treeview.netlify.app/)

onelinerhub: [view

How do I create a treeview with Vue.js?](https://onelinerhub.com/vue.js/view--how-do-i-create-a-treeview-with-vue-js)