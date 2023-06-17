# How do I use jQuery to zip files?
// plain

jQuery is a JavaScript library that is used to create interactive web applications. It can be used to create a zip file from a folder or multiple files. To do this, you will need to include the [jszip](https://github.com/Stuk/jszip) library.

Include the library in your HTML file:
```html
<script src="jszip.js"></script>
```

Then in your JavaScript file, you can use the following code to create a zip file from a folder:
```js
// create a new JSZip object
var zip = new JSZip();

// add a folder to the zip file
zip.folder("myFolder");

// add files to the zip file
zip.file("myFile.txt", "This is a text file");

// generate the zip file and save it
zip.generateAsync({type:"blob"})
  .then(function(content) {
    saveAs(content, "myZipFile.zip");
  });
```

This will generate a zip file called `myZipFile.zip` that contains a folder called `myFolder` and a file called `myFile.txt`.

You can also add multiple files to the zip file by looping through an array of file objects:
```js
// create a new JSZip object
var zip = new JSZip();

// array of files
var files = [
  {name: "myFile1.txt", content: "This is the first text file"},
  {name: "myFile2.txt", content: "This is the second text file"}
];

// loop through files array and add each file to the zip file
files.forEach(function(file) {
  zip.file(file.name, file.content);
});

// generate the zip file and save it
zip.generateAsync({type:"blob"})
  .then(function(content) {
    saveAs(content, "myZipFile.zip");
  });
```

This will generate a zip file called `myZipFile.zip` that contains two files called `myFile1.txt` and `myFile2.txt`.

You can find more examples and documentation on the [jszip](https://github.com/Stuk/jszip) library.

onelinerhub: [How do I use jQuery to zip files?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-zip-files)