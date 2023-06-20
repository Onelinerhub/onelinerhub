# How do I integrate Yandex Maps with Vue.js?
// plain

Integrating Yandex Maps with Vue.js is relatively straightforward. First, install the [Yandex Maps API for JavaScript](https://tech.yandex.com/maps/doc/jsapi/2.1/quick-start/index-docpage/) by including the following code in the HTML page of your Vue.js application:

```
<script src="https://api-maps.yandex.ru/2.1/?lang=en_US" type="text/javascript"></script>
```

Then, create a Vue component to represent the map. In the `<script>` tag, use the `mounted` hook to create a new Yandex Map instance. For example:

```
<script>
export default {
  name: 'Map',
  mounted() {
    this.myMap = new ymaps.Map('map', {
      center: [55.75, 37.57],
      zoom: 10
    });
  }
};
</script>
```

Finally, add a `<div>` to the `<template>` tag to contain the map.

```
<template>
  <div>
    <div id="map"></div>
  </div>
</template>
```

The result is a fully functional Yandex Map embedded in your Vue.js application.

## Helpful links
- [Yandex Maps API for JavaScript](https://tech.yandex.com/maps/doc/jsapi/2.1/quick-start/index-docpage/)
- [Vue.js Lifecycle Hooks](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)

onelinerhub: [How do I integrate Yandex Maps with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-integrate-yandex-maps-with-vue-js)