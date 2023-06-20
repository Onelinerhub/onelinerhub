# chart

How do I create an organizational chart using Vue.js?
// plain

Creating an organizational chart using Vue.js is a straightforward process. The following example code will create a basic organizational chart with a root node and two children.

```
<template>
  <div>
    <OrganizationalChart :data="data"/>
  </div>
</template>

<script>
import OrganizationalChart from 'vue-orgchart'

export default {
  components: {
    OrganizationalChart
  },
  data() {
    return {
      data: {
        name: 'Root',
        children: [
          {
            name: 'Child 1'
          },
          {
            name: 'Child 2'
          }
        ]
      }
    }
  }
}
</script>
```

This code will create an organizational chart with the root node labeled "Root" and two children labeled "Child 1" and "Child 2". The code consists of a template section, which is used to render the chart, and a script section, which contains the data for the chart. The data is stored in a variable called "data" and is an object with a "name" property and a "children" property, which is an array of objects with "name" properties.

The components section imports the OrganizationalChart component from the vue-orgchart library. The data section creates an object with the properties "name" and "children". The template section renders the chart using the OrganizationalChart component and passing in the "data" object.

## Helpful links

- https://github.com/jackmoody11/vue-orgchart
- https://vuejs.org/v2/guide/components.html

onelinerhub: [chart

How do I create an organizational chart using Vue.js?](https://onelinerhub.com/vue.js/chart--how-do-i-create-an-organizational-chart-using-vue-js)