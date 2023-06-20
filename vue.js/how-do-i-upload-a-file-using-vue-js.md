# How do I upload a file using Vue.js?
// plain

Using Vue.js, you can upload files by using `v-on` to listen for a file input event, then using `FormData` to package the file data.

## Example code

```
<input type="file" v-on:change="onFileChange">

...

methods: {
  onFileChange(e) {
    let files = e.target.files || e.dataTransfer.files;
    if (!files.length)
      return;
    this.createImage(files[0]);
  },
  createImage(file) {
    let reader = new FileReader();
    let vm = this;
    reader.onload = (e) => {
      vm.image = e.target.result;
    };
    reader.readAsDataURL(file);
  }
}
```

Then, to actually upload the file, you can use `FormData` to package the file data and send it to your server.

## Example code

```
let formData = new FormData();
formData.append('file', file);

axios.post('/upload', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
})
.then(response => {
  console.log(response);
})
.catch(error => {
  console.log(error);
})
```

The code above will send a POST request to `/upload` with the file data included in the request body. The response will be logged to the console.

Parts of the code:
- `<input type="file" v-on:change="onFileChange">` - listens for a file input event
- `onFileChange(e)` - handles the file input event
- `createImage(files[0])` - creates an image from the file
- `let formData = new FormData()` - creates a new FormData object
- `formData.append('file', file)` - adds the file data to the FormData object
- `axios.post('/upload', formData, {...})` - sends a POST request with the FormData object in the request body
- `console.log(response)` - logs the response to the console

## Helpful links
- [Vue.js File Uploads](https://vuejs.org/v2/examples/file-upload.html)
- [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
- [Axios](https://github.com/axios/axios)

onelinerhub: [How do I upload a file using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-upload-a-file-using-vue-js)