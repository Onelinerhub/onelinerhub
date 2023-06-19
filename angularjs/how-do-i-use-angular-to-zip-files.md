# How do I use Angular to zip files?
// plain

Angular is a JavaScript framework used to build web applications. It can be used to zip files by using the JavaScript library [JSZip](https://stuk.github.io/jszip/). The following example code shows how to use JSZip to zip a file in Angular:

```
// Create a new instance of JSZip
let zip = new JSZip();

// Add a file to the zip
zip.file("hello.txt", "Hello World");

// Generate the zip file
let zipFile = zip.generateAsync({ type: "blob" });

// Create a download link
let downloadLink = document.createElement("a");
downloadLink.href = window.URL.createObjectURL(zipFile);
downloadLink.download = "example.zip";
downloadLink.click();
```

This code creates a new instance of JSZip, adds a file called `hello.txt` with the content `Hello World` to the zip, generates the zip file as a blob, and creates a download link for the zip file.

## Code explanation


- `let zip = new JSZip();`: creates a new instance of JSZip
- `zip.file("hello.txt", "Hello World");`: adds a file to the zip
- `let zipFile = zip.generateAsync({ type: "blob" });`: generates the zip file
- `let downloadLink = document.createElement("a");`: creates a download link element
- `downloadLink.href = window.URL.createObjectURL(zipFile);`: sets the download link href to the zip file
- `downloadLink.download = "example.zip";`: sets the download link file name
- `downloadLink.click();`: triggers the download of the zip file

onelinerhub: [How do I use Angular to zip files?](https://onelinerhub.com/angularjs/how-do-i-use-angular-to-zip-files)