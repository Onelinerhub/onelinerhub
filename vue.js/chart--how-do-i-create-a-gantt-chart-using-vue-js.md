# chart

How do I create a Gantt chart using Vue.js?
// plain

A Gantt chart can be created using Vue.js by utilizing the [Vue-Gantt](https://github.com/lucasto-dev/vue-gantt) library. This library provides a simple and intuitive way to create Gantt charts using Vue.js.

To create a Gantt chart using Vue-Gantt, you will need to include the Vue-Gantt library in your project, as well as the Vue.js library. After that, you can use the following code example to create a basic Gantt chart:

```
<template>
  <vue-gantt
    :data="data"
    :columns="columns"
    :options="options"
  />
</template>

<script>
  import VueGantt from 'vue-gantt'

  export default {
    components: {
      VueGantt
    },
    data () {
      return {
        data: [
          {
            id: 1,
            name: 'Task 1',
            start: '2020-01-01',
            end: '2020-01-05'
          },
          {
            id: 2,
            name: 'Task 2',
            start: '2020-01-02',
            end: '2020-01-07'
          }
        ],
        columns: [
          {
            label: 'Name',
            field: 'name',
            width: 200
          },
          {
            label: 'Start',
            field: 'start',
            width: 200
          },
          {
            label: 'End',
            field: 'end',
            width: 200
          }
        ],
        options: {
          barHeight: 20
        }
      }
    }
  }
</script>
```

This code will create a Gantt chart with two tasks, each with a name, start date, and end date. The columns variable defines the column names and widths, while the options variable can be used to customize the Gantt chart.

## Helpful links
- [Vue-Gantt](https://github.com/lucasto-dev/vue-gantt)
- [Vue.js](https://vuejs.org/)

onelinerhub: [chart

How do I create a Gantt chart using Vue.js?](https://onelinerhub.com/vue.js/chart--how-do-i-create-a-gantt-chart-using-vue-js)