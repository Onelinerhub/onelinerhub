# How do I download a zip file using Vue.js?
// plain

To download a zip file using Vue.js, you can use the [JSZip](https://stuk.github.io/jszip/) library.

First, include the library in your project by adding the following code to the `<head>` section of your HTML file:

```html
<script src="https://stuk.github.io/jszip/dist/jszip.js"></script>
```

Then, you can use the following code to download the zip file:

```js
import JSZip from 'jszip';

let zip = new JSZip();

// Add files to the zip
zip.file("Hello.txt", "Hello World\n");

// Generate the zip file asynchronously
zip.generateAsync({type:"blob"})
.then(function(content) {
    // see FileSaver.js
    saveAs(content, "example.zip");
});
```

The code above will generate a zip file containing the file `Hello.txt` with the content `Hello World` and download it as `example.zip`.

## Helpful links
- [JSZip](https://stuk.github.io/jszip/)
- [FileSaver.js](https://github.com/eligrey/FileSaver.js/)

onelinerhub: [How do I download a zip file using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-download-a-zip-file-using-vue-js)