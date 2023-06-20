# generation

How can I generate a PDF using Vue.js?
// plain

Generating a PDF using Vue.js is possible with the help of a library such as [Vue-PDF](https://vue-pdf.org/). To use this library, you will need to install it into your project:

```
npm install vue-pdf
```

Once installed, you can create a PDF from a Vue component by using the `<pdf>` tag. For example:

```
<template>
  <pdf :src="src" :page="page"></pdf>
</template>

<script>
import Pdf from 'vue-pdf'

export default {
  components: {
    Pdf
  },
  data() {
    return {
      src: 'path/to/pdf',
      page: 1
    }
  }
}
</script>
```

This code will create a PDF from the source file `path/to/pdf` with the page number `1`.

The `<pdf>` tag supports a number of props to customize the PDF, such as:

- `src`: The URL or base64 string of the PDF file.
- `page`: The page number to display.
- `scale`: The scale of the PDF page.
- `rotate`: The rotation of the PDF page.

For more information on how to use `Vue-PDF`, refer to the [official documentation](https://vue-pdf.org/).

onelinerhub: [generation

How can I generate a PDF using Vue.js?](https://onelinerhub.com/vue.js/generation--how-can-i-generate-a-pdf-using-vue-js)