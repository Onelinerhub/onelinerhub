# How can I use Vue.js and React.js together in a single project?
// plain

Vue.js and React.js can be used together in a single project by using the [React-Vue](https://github.com/vuejs/react-vue) library. This library allows us to embed Vue components into React components and vice versa.

For example, with the following code:

```js
import React from 'react'
import { render, createElement } from 'react-vue'
import MyVueComponent from './MyVueComponent.vue'

const MyReactComponent = () => {
  return createElement(MyVueComponent, {
    props: {
      message: 'Hello World!'
    }
  })
}

render(<MyReactComponent />, document.getElementById('root'))
```

We can render a Vue component (`MyVueComponent`) inside a React component (`MyReactComponent`) and pass props to it.

## Code explanation

- `import React from 'react'` - imports the React library.
- `import { render, createElement } from 'react-vue'` - imports the `render` and `createElement` functions from the `react-vue` library.
- `import MyVueComponent from './MyVueComponent.vue'` - imports the `MyVueComponent` Vue component from the `MyVueComponent.vue` file.
- `const MyReactComponent = () => { ... }` - defines a React component named `MyReactComponent`.
- `return createElement(MyVueComponent, { ... })` - inside the `MyReactComponent` component, we call the `createElement` function from the `react-vue` library to create an element from the imported `MyVueComponent` Vue component.
- `render(<MyReactComponent />, document.getElementById('root'))` - calls the `render` function from the `react-vue` library to render the `MyReactComponent` React component inside the DOM element with the `id` of `root`.

## Helpful links
- [React-Vue](https://github.com/vuejs/react-vue)
- [Using React and Vue Together](https://dzone.com/articles/using-react-and-vue-together)

onelinerhub: [How can I use Vue.js and React.js together in a single project?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-and-react-js-together-in-a-single-project)