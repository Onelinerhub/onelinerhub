# How can I integrate Vue.js with Yii2?
// plain

Integrating Vue.js with Yii2 is relatively easy.

First, you need to include the `Vue.js` script in your Yii2 application. This can be done by adding the following code to the `<head>` section of the layout file:

```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

Once the `Vue.js` script is included, you can create a new Vue instance and bind it to a DOM element using the `el` property. For example:

```
<div id="app">
  {{ message }}
</div>

<script>
  var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  })
</script>
```

This will create a new Vue instance and bind it to the `app` element. The output of the above code will be:

```
Hello Vue!
```

Finally, you can use Yii2's `renderPartial()` method to render a Vue component from a view file. For example:

```
<?php echo \yii\helpers\Html::renderPartial('_vue-component'); ?>
```

This will render the `_vue-component` view file and the Vue component will be available for use inside the Yii2 application.

## Helpful links
- https://vuejs.org/
- https://www.yiiframework.com/doc/guide/2.0/en/start-installation

onelinerhub: [How can I integrate Vue.js with Yii2?](https://onelinerhub.com/vue.js/how-can-i-integrate-vue-js-with-yii-)