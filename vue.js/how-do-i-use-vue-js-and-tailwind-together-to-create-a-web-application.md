# How do I use Vue.js and Tailwind together to create a web application?
// plain

To use Vue.js and Tailwind together to create a web application, you will need to include the Tailwind CSS library in your Vue project.

You can do this by adding the following line to your HTML file:
```<link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">```

You can then use Tailwind classes in your components. For example, if you want to create a simple button you can use the following code in your template:
```
<template>
  <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    Button
  </button>
</template>
```

This will create a blue button with white text when rendered.

To make use of Tailwind's utility classes you will need to use the Tailwind CSS classes in your component's style section. For example, you could add the following code to your component's style section:
```
<style>
  .my-class {
    @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded;
  }
</style>
```

This will create a class called 'my-class' with the same styles as the button example above.

## Helpful links
- [Tailwind CSS Documentation](https://tailwindcss.com/docs/installation/)
- [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [How do I use Vue.js and Tailwind together to create a web application?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-and-tailwind-together-to-create-a-web-application)