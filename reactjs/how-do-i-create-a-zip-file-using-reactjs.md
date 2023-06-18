# How do I create a zip file using ReactJS?
// plain

Creating a zip file using ReactJS is possible using the [jszip](https://stuk.github.io/jszip/) library.

To create a zip file, first install the library via npm:

`npm install jszip`

Then, you can import the library into your React component:

```
import JSZip from 'jszip';
```

Next, you can create a new Zip object and add files to it:

```
let zip = new JSZip();
zip.file("Hello.txt", "Hello World\n");
```

Finally, you can generate the zip file and save it to disk:

```
zip.generateAsync({type:"blob"})
    .then(function (blob) {
        saveAs(blob, "example.zip");
    });
```

This code will create a zip file named `example.zip` and save it to the user's device.

Parts of the code:

1. `npm install jszip`: Installs the jszip library.
2. `import JSZip from 'jszip'`: Imports the library into the React component.
3. `let zip = new JSZip()`: Creates a new Zip object.
4. `zip.file("Hello.txt", "Hello World\n")`: Adds a file named `Hello.txt` with contents `Hello World\n` to the Zip object.
5. `zip.generateAsync({type:"blob"})`: Generates the zip file.
6. `saveAs(blob, "example.zip")`: Saves the zip file to the user's device.

## Helpful links

- [jszip](https://stuk.github.io/jszip/)

onelinerhub: [How do I create a zip file using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-zip-file-using-reactjs)