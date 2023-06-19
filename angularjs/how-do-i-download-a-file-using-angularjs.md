# How do I download a file using AngularJS?
// plain

The following example demonstrates how to download a file using AngularJS:

```
// Create a new instance of the http service
var http = new XMLHttpRequest();

// Set the url of the file you want to download
http.open("GET", "http://example.com/file.txt", true);

// Set the response type to blob
http.responseType = "blob";

// Send the request
http.send();

// When the request is complete
http.onload = function() {
    // Create a new Blob object using the response data of the onload object
    var blob = new Blob([http.response], {type: "text/plain"});

    // Create a link element, hide it, direct it towards the blob, and then 'click' it programatically
    var a = document.createElement("a");
    a.style = "display: none";
    document.body.appendChild(a);
    // Create a DOMString representing the blob and point the link element towards it
    var url = window.URL.createObjectURL(blob);
    a.href = url;
    a.download = "file.txt";
    // Programatically click the link to trigger the download
    a.click();
    // Release the reference to the file by revoking the Object URL
    window.URL.revokeObjectURL(url);
}
```

This code will create an instance of the http service, set the url of the file to be downloaded, set the response type to blob, send the request, create a new Blob object using the response data, create a link element, create a DOMString representing the blob and point the link element towards it, programatically click the link to trigger the download, and then release the reference to the file by revoking the Object URL.

## Code explanation


1. Create a new instance of the http service: `var http = new XMLHttpRequest();`
2. Set the url of the file you want to download: `http.open("GET", "http://example.com/file.txt", true);`
3. Set the response type to blob: `http.responseType = "blob";`
4. Send the request: `http.send();`
5. Create a new Blob object using the response data: `var blob = new Blob([http.response], {type: "text/plain"});`
6. Create a link element, hide it, direct it towards the blob, and then 'click' it programatically: `var a = document.createElement("a"); a.style = "display: none"; document.body.appendChild(a);`
7. Create a DOMString representing the blob and point the link element towards it: `var url = window.URL.createObjectURL(blob); a.href = url; a.download = "file.txt";`
8. Programatically click the link to trigger the download: `a.click();`
9. Release the reference to the file by revoking the Object URL: `window.URL.revokeObjectURL(url);`

## Helpful links

- [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)
- [URL.createObjectURL()](https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL)
- [URL.revokeObjectURL()](https://developer.mozilla.org/en-US/docs/Web/API/URL/revokeObjectURL)

onelinerhub: [How do I download a file using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-download-a-file-using-angularjs)