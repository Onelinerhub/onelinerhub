# How do I use the FileReader API in Vue.js?
// plain

The FileReader API is a powerful tool for reading and manipulating files in Vue.js. It allows you to read the contents of a file, create a Blob from the file, and create a data URL representing the file's data. The following example code can be used to read a file and display its contents:

```
<template>
  <div>
    <input type="file" @change="onFileChange">
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: ''
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createFile(files[0]);
    },
    createFile(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.text = e.target.result;
      };
      reader.readAsText(file);
    }
  }
};
</script>
```

The code above will display the contents of the file as plain text in the `<p>` tag.

The code consists of the following parts:

1. `<input type="file" @change="onFileChange">` - This is an HTML input element with the type set to `file` and an event listener for the `change` event, which triggers the `onFileChange` method.

2. `onFileChange(e) { ... }` - This is the method that is called when the `change` event is triggered on the input element. It retrieves the files from the event object and then calls the `createFile` method with the first file.

3. `createFile(file) { ... }` - This method creates a new `FileReader` object and sets an event listener for the `load` event. When the `load` event is triggered, the `text` data property is set with the result of the `readAsText` method.

For more information, please refer to the following resources:

- [FileReader API](https://developer.mozilla.org/en-US/docs/Web/API/FileReader)
- [Vue.js FileReader API](https://vuejs.org/v2/guide/file-upload.html#Using-the-FileReader-API)

onelinerhub: [How do I use the FileReader API in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-filereader-api-in-vue-js)